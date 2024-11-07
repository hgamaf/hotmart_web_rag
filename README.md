# 🌐 FastAPI Hotmart QA Service

Este é um serviço de perguntas e respostas desenvolvido com **FastAPI** que permite ao usuário realizar perguntas sobre a plataforma **Hotmart**. Ele utiliza embeddings e um índice **FAISS** para retornar respostas relevantes.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado: 🐍 **Python 3.9+**, 🐋 **Docker** (opcional, para rodar em contêiner) e 📦 **Virtualenv** (recomendado para ambiente isolado).

## ⚙️ Configuração

### Instruções de Configuração do Projeto
#### 1. Clone o repositório
```bash
git clone https://github.com/hgamaf/hotmart_web_rag.git
```

#### 2. Vá para a pasta da aplicação
```bash
cd hotmart_web_rag
```

#### 3. Crie e ative um ambiente virtual
###### Criando .venv o Windows ou Mac:
```bash
python -m venv .venv
```

###### Ativando .venv o Windows:
```bash
.venv\Scripts\activate
```

###### Ativando .venv o Mac:
```bash
source .venv/bin/activate
```

#### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

#### 5. Configure as variáveis de ambiente
```bash
echo # Variáveis de ambiente >> .env
```

##### Abra o arquivo .env em um editor de texto e adicione a chave da API do OpenAI
##### Exemplo: OPENAI_API_KEY=your_openai_api_key

## 🚀 Executando com FastAPI

Para iniciar o servidor FastAPI localmente, execute o comando `uvicorn main:app --reload`. A aplicação estará disponível em [http://localhost:8000](http://localhost:8000).

![image](https://github.com/user-attachments/assets/7ef22cbe-2b79-497a-bca4-5a3b70a0f876)

## 🐳 Executando com Docker

Se preferir, você pode rodar a aplicação em um contêiner Docker.

### Passos para execução:

1. **ATENÇÃO**! Você deve inicializar o Docker Desktop
2. 📦 Construa a imagem com `docker-compose build`.
3. ▶️ Execute o contêiner com `docker-compose up`.
4. A aplicação estará disponível em [http://localhost:8000](http://localhost:8000) e pronta para receber requisições.

![image](https://github.com/user-attachments/assets/86b83172-efc7-423d-8c7b-ed8be67d2017)


## 📑 Documentação da API

A documentação interativa do FastAPI pode ser acessada: 📘 **Swagger**: [http://localhost:8000/docs](http://localhost:8000/docs) e 📕 **Redoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc).

## 🔗 Endpoints

### 1. 🔍 `GET /`
**Descrição**: Endpoint inicial para verificar se a aplicação está funcionando. Exemplo de `curl`: `curl -X 'GET' 'http://localhost:8000/' -H 'accept: application/json'`. Resposta esperada: `{"message": "Bem-vindo ao serviço de documentos e perguntas!"}`.

### 2. 📚 `GET /load_documents`
**Descrição**: Carrega documentos da Hotmart e cria um índice FAISS para consultas. Exemplo de `curl`: `curl -X 'GET' 'http://localhost:8000/load_documents' -H 'accept: application/json'`. Resposta esperada: `{"status": "Documentos carregados e indexados com sucesso"}`.

### 3. ❓ `POST /ask_question`
**Descrição**: Faz uma pergunta sobre a Hotmart e retorna a resposta com base nos documentos carregados. Exemplo de `curl`: `curl -X 'POST' 'http://localhost:8000/ask_question' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{ "question": "Quem pode ser produtor?" }'`. Parâmetro: `question` (string) - A pergunta que o usuário deseja fazer sobre a Hotmart. Resposta esperada: `{"answer": "Resposta gerada pelo modelo de IA com base nos documentos"}`.



🎉 Com este guia, você tem tudo o que precisa para configurar, executar e utilizar sua aplicação FastAPI. Qualquer ajuste ou personalização adicional pode ser facilmente implementado conforme necessário. 📫 Dúvidas? Sinta-se à vontade para contribuir ou entrar em contato!
