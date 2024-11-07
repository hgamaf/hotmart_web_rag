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

Se preferir, você pode rodar a aplicação em um contêiner Docker para simplificar a configuração e garantir que todas as dependências estejam isoladas.

### Passos para execução:

1. **ATENÇÃO**: Certifique-se de que o Docker Desktop está ativo.
   - Antes de prosseguir, abra o Docker Desktop e aguarde até que ele esteja totalmente iniciado.

2. 📦 **Construa a imagem Docker**:
   - No terminal, dentro do diretório do projeto, execute o comando abaixo para construir a imagem Docker:
     ```bash
     docker-compose build
     ```
   - Este comando prepara todos os componentes necessários para a aplicação funcionar no contêiner.

3. ▶️ **Inicie o contêiner Docker**:
   - Após a construção da imagem, inicie o contêiner com o comando:
     ```bash
     docker-compose up
     ```
   - Esse comando inicia a aplicação no contêiner e a mantém em execução.

4. **Verifique o status**:
   - Quando o contêiner estiver em execução, a aplicação estará disponível em [http://localhost:8000](http://localhost:8000).
   - Aguarde até que o terminal confirme que a aplicação está rodando e pronta para receber requisições.


## 🧪 Como testar?

Após a aplicação estar rodando no Docker, você pode verificar se ela está funcionando corretamente enviando uma pergunta para o endpoint. Abaixo está um exemplo de `curl` que pode ser executado somente **após** os passos acima:

### Exemplo de `curl` para a pergunta "O que são hotleads?"

1. No terminal, execute o comando abaixo para enviar uma pergunta à aplicação:
   ```bash
   curl -X 'POST' 'http://localhost:8000/ask_question' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{ "question": "O que são hotleads?" }'
   ```



