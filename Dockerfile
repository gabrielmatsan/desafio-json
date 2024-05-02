FROM ubuntu:latest

# Instala o python
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Copia o teste.py para o container meu_ubuntu
COPY teste.py /app/teste.py

WORKDIR /app

# Executa os seguintes comandos ao iniciar a aplicacao
CMD ["python3", "teste.py"]
