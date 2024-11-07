# FastAPI Hotmart QA Service

Este é um serviço de perguntas e respostas desenvolvido com **FastAPI** que permite ao usuário realizar perguntas sobre a plataforma **Hotmart**. Ele utiliza embeddings e um índice **FAISS** para retornar respostas relevantes.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado: **Python 3.9+**, **Docker** (opcional, para rodar em contêiner) e **Virtualenv** (recomendado para ambiente isolado).

## Configuração

1. Clone o repositório com `git clone https://github.com/seu-usuario/seu-repositorio.git` e navegue até ele com `cd seu-repositorio`.
2. Crie e ative um ambiente virtual com `python3 -m venv .venv` e `source .venv/bin/activate`.
3. Instale as dependências com `pip install -r requirements.txt`.
4. Configure as variáveis de ambiente criando um arquivo `.env` na raiz do projeto com a chave da API do OpenAI: `OPENAI_API_KEY=your_openai_api_key`.

## Executando a Aplicação

Para iniciar o servidor FastAPI localmente, execute o comando `uvicorn tests.main:app --reload`. A aplicação estará disponível em `http://localhost:8000`.

## Documentação da API

A documentação interativa do FastAPI pode ser acessada em Swagger: [http://localhost:8000/docs](http://localhost:8000/docs) e Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc).

## Endpoints

1. `GET /` - Endpoint inicial para verificar se a aplicação está funcionando. Exemplo de `curl`: `curl -X 'GET' 'http://localhost:8000/' -H 'accept: application/json'`. Resposta esperada: `{"message": "Bem-vindo ao serviço de documentos e perguntas!"}`.

2. `GET /load_documents` - Carrega documentos da Hotmart e cria um índice FAISS para consultas. Exemplo de `curl`: `curl -X 'GET' 'http://localhost:8000/load_documents' -H 'accept: application/json'`. Resposta esperada: `{"status": "Documentos carregados e indexados com sucesso"}`.

3. `POST /ask_question` - Faz uma pergunta sobre a Hotmart e retorna a resposta com base nos documentos carregados. Exemplo de `curl`: `curl -X 'POST' 'http://localhost:8000/ask_question' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{ "question": "Quem pode ser produtor?" }'`. Parâmetro: `question` (string) - A pergunta que o usuário deseja fazer sobre a Hotmart. Resposta esperada: `{"answer": "Resposta gerada pelo modelo de IA com base nos documentos"}`.

## Executando com Docker

Se preferir, você pode rodar a aplicação em um contêiner Docker.

### Passos para execução:

1. Construa a imagem com `docker-compose build`.
2. Execute o contêiner com `docker-compose up`. A aplicação estará disponível em `http://localhost:8000` e pronta para receber requisições.

---

Com este guia, os usuários terão instruções completas para configurar, executar e utilizar sua aplicação FastAPI. Qualquer ajuste ou personalização adicional pode ser facilmente implementado conforme necessário.
