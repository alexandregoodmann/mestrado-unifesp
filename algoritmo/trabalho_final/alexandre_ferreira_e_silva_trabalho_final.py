# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Trabalho final do semestre
# Fonte: ChatGPT, Google Gemini
# --------------------------------------------------------------------------------------

import os
import hashlib
import time
from hash_encadeamento import HashEncadeamento
from arvore_avl import inserirAVL, pesquisarAVL
from tabulate import tabulate # >>>>>> pip install tabulate 
os.system('cls' if os.name == 'nt' else 'clear')

import uuid

# ------------------------------------------------------------------------------------------------------
# ABRIR MASSA DE DADOS
# Arquivo com 10 mil chaves UUID
# ------------------------------------------------------------------------------------------------------
arquivo = open("C:\\projetos\\mestrado-unifesp\\algoritmo\\trabalho_final\\base_dados.txt", "r")  # Abre o arquivo para escrita
linhas = arquivo.readlines()
arquivo.close()  # Fecha o arquivo

# ------------------------------------------------------------------------------------------------------
# HASH ENCADEAMENTO
# Inserir as chaves em uma tabela Hash
# ------------------------------------------------------------------------------------------------------
tempo_insercao = []
tabela_encadeamento = HashEncadeamento(100000)
start_time = time.time()
for linha in linhas:
    time_low = uuid.UUID(str(linha).replace('\n', '')).time_low
    tabela_encadeamento.insert(time_low, linha)
tempo_insercao_encadeamento =  {time.time() - start_time}
tempo_insercao.append(['Hash Table', tempo_insercao_encadeamento])

# ------------------------------------------------------------------------------------------------------
# HASH SEARCH
# Essas chaves estao nas respectivas posições dentro do arquivo de dados:
# posição 200k, 400k, 600k, 800k, 1M
# ------------------------------------------------------------------------------------------------------
tempo_busca = [
    ['9325c992-a9ed-11ef-99ef-d89c67ddb1a4', None, None],
    ['93b5fe16-a9ed-11ef-8d2a-d89c67ddb1a4', None, None],
    ['9451ad87-a9ed-11ef-8bd1-d89c67ddb1a4', None, None],
    ['94e48951-a9ed-11ef-9eef-d89c67ddb1a4', None, None],
    ['9572be89-a9ed-11ef-8c1e-d89c67ddb1a4', None, None]
]

for item in tempo_busca:
    start_time = time.time()
    key = uuid.UUID(item[0]).time_low
    chave = tabela_encadeamento.search(key)
    tempo_search_chave =  {time.time() - start_time}
    item[1] = tempo_search_chave

# -----------------------------------------------
# ÁRVORE BINÁRIA AVL
# -----------------------------------------------
root = None
start_time = time.time()
for linha in linhas:
    valor = uuid.UUID(str(linha).replace('\n', '')).time_low
    root = inserirAVL(root, valor)
tempo_insercao_avl =  {time.time() - start_time}
tempo_insercao.append(['AVL', tempo_insercao_avl])

for item in tempo_busca:
    start_time = time.time()
    key = uuid.UUID(item[0]).time_low
    pesquisarAVL(root, key)
    tempo_search_avl =  {time.time() - start_time}
    item[2] = tempo_search_avl

# -----------------------------------------------
# RESULTADOS
# -----------------------------------------------
print(tabulate(tempo_insercao))
tempo_busca.insert(0,['Chave', 'Tempo de Busca Hash', 'Tempo Busca AVL'])
print(tabulate(tempo_busca))
