from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.document_loaders import WebBaseLoader
import os
from openai import OpenAI
import faiss
import numpy as np
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurar o cliente Azure OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Inicializar o FastAPI
app = FastAPI()

# URL fixa da Hotmart
HOTMART_URL = ["https://hotmart.com/pt-br/blog/como-funciona-hotmart/"]

# Modelos Pydantic para os endpoints
class QuestionRequest(BaseModel):
    question: str

# Funções auxiliares para carregamento e geração de embeddings
def load_documents(urls):
    loader = WebBaseLoader(urls)
    return loader.load()

def chunk_text(text, max_tokens=4000):
    words = text.split()
    chunks, current_chunk, current_length = [], [], 0
    
    for word in words:
        if current_length + len(word) + 1 <= max_tokens:
            current_chunk.append(word)
            current_length += len(word) + 1
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk, current_length = [word], len(word) + 1
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks

def create_embedding(text):
    response = client.embeddings.create(input=text, model="text-embedding-3-small")
    return np.array(response.data[0].embedding).astype("float32")

def generate_embeddings(documents):
    all_embeddings = []
    
    for doc in documents:
        chunks = chunk_text(doc.page_content)
        for chunk in chunks:
            embedding = create_embedding(chunk)
            all_embeddings.append(embedding)
    
    embeddings = np.array(all_embeddings).astype("float32")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    
    return index

def generate_question_embedding(question):
    return create_embedding(question)

def search_index(index, question_embedding, top_k=5):
    distances, indices = index.search(np.array([question_embedding]), top_k)
    return [idx for idx in indices[0] if idx >= 0]

def get_relevant_texts(documents, indices):
    return " ".join(documents[i].page_content for i in indices if i < len(documents))

def ask_gpt4o(question, index, documents, top_k=5):
    question_embedding = generate_question_embedding(question)
    indices = search_index(index, question_embedding, top_k)
    
    if not indices:
        return "Nenhum documento relevante encontrado para responder à pergunta."
    
    context = get_relevant_texts(documents, indices)
    messages = [
        {"role": "system", "content": "Você é um assistente especializado em responder apenas perguntas sobre a Hotmart com única e exclusivamente baseado em informações fornecidas."},
        {"role": "user", "content": f"Com base nas seguintes informações: {context}\n\nPergunta: {question}"}
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o", 
        messages=messages, 
        max_tokens=150, 
        temperature=0.7
    )
    
    return response.choices[0].message.content.strip()

@app.get("/")
async def root():
    return {"message": "Bem-vindo ao serviço de documentos e perguntas!"}

# Endpoint para carregar documentos e criar o índice FAISS
@app.get("/load_documents")
async def load_and_index_documents():
    try:
        documents = load_documents(HOTMART_URL)
        index = generate_embeddings(documents)
        return {"status": "Documentos carregados e indexados com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para fazer uma pergunta
@app.post("/ask_question")
async def ask_question(request: QuestionRequest):
    try:
        documents = load_documents(HOTMART_URL)  # Carregar documentos novamente
        index = generate_embeddings(documents)  # Recriar índice FAISS
        answer = ask_gpt4o(request.question, index, documents)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))