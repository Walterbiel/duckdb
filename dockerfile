# Use a imagem base Python 3.12
FROM python:3.12

# Instale o Poetry
RUN pip install poetry

# Copie os arquivos do projeto para o diretório /src dentro do container
COPY . /src

# Defina o diretório de trabalho como /src
WORKDIR /src

# Instale as dependências do projeto usando Poetry
RUN poetry install

# Exponha a porta 8501 para o Streamlit
EXPOSE 8501

# Configure o ponto de entrada para iniciar o Streamlit
ENTRYPOINT ["poetry", "run", "streamlit", "run", "app.py", "--server.port=8501"]
