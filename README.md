# Uso do Docker com script Python em um contêiner Linux (Ubuntu)

Este guia descreve como rodar um script Python dentro de um contêiner Docker baseado em Ubuntu, que interage com diretórios e arquivos locais, criando um arquivo JSON.

## Pré-requisitos

Antes de começar, certifique-se de que o Docker e o Docker Compose estejam instalados em sua máquina. O código e os Dockerfiles necessários devem estar clonados de um repositório git.

## Instruções

1. **Preparação do Ambiente**:
   Após clonar o repositório, você pode precisar fazer uma limpeza inicial dos diretórios que serão gerados pelo script Python. Se existirem, apague as pastas `main` e `data`.

2. **Construção do Contêiner**:
   Abra o terminal e navegue até o diretório do projeto. Use o seguinte comando para construir a imagem do contêiner a partir do Dockerfile:
   ```bash
   docker-compose build
   docker-compose up

3. **Final**:
   Após isso, o arquivo JSON foi criado dentro da pasta main, que foi gerada novamente, junto com o pasta data.

