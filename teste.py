import os
import json
import time

inicio = time.time()
# Dados a serem escritos no arquivo JSON
data = {
    "nome": "Gabriel",
    "idade": 22,
    "Curso": "BCC",
    "Semetre": 3
}

# Caminho do diretório onde o arquivo será salvo
diretorio = './main'

# Cria o diretório se ele não existir
os.makedirs(diretorio, exist_ok=True)

# Caminho completo do arquivo
caminho_arquivo = os.path.join(diretorio, 'data.json')

# Escreve os dados no arquivo JSON
with open(caminho_arquivo, 'w') as f:
    json.dump(data, f)

final = time.time() - inicio
print(final)