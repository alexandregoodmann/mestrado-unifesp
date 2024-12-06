# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Trabalho final do semestre
# Fonte: ChatGPT, Google Gemini
# --------------------------------------------------------------------------------------

import os
import time
import csv
import uuid
from hash_encadeamento import HashEncadeamento
from arvore_avl import inserirAVL, pesquisarAVL
from tabulate import tabulate # >>>>>> pip install tabulate 
os.system('cls' if os.name == 'nt' else 'clear')

# ------------------------------------------------------------------------------------------------------
# METODO PARA FORMATAR NUMERO
# ------------------------------------------------------------------------------------------------------
def formatNumber(number):
    scaled_number = number * 1e6
    return f"{scaled_number:.4f}"
# ------------------------------------------------------------------------------------------------------
# ABRIR MASSA DE DADOS
# Arquivo com 296 mil registros
# ------------------------------------------------------------------------------------------------------
lista_uuid = []
chaves_busca = []
tempos_insert = [['Tamanho Tabela Hash', 'Tempo(s)']]
tempos_busca = [['Tamanho', 'Chave 1', 'Chave 2', 'Chave 3', 'Chave 4', 'Chave 5']]

print('--- Fazendo a leitura dos dados ---')

with open("trabalho_final\Emendas-Parlamentares.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=";")
    for qtd, linha in enumerate(arquivo_csv):
        key = uuid.uuid1(int(linha[9]))
        lista_uuid.append(key)
        if (qtd % 60000 == 0):
            chaves_busca.append(key)
# ------------------------------------------------------------------------------------------------------
# ÁRVORE BINÁRIA AVL - INSERT
# ------------------------------------------------------------------------------------------------------
print('--- Fazendo insert na Árvore AVL ---')
root = None
start_time = time.time()
for linha in lista_uuid:
    valor = uuid.UUID(str(linha).replace('\n', '')).time_low
    root = inserirAVL(root, valor)
tempo_insercao_avl =  {time.time() - start_time}.pop()
tempos_insert.append(['AVL', f"{tempo_insercao_avl:2f}"])
# ------------------------------------------------------------------------------------------------------
# ÁRVORE BINÁRIA AVL - BUSCA
# ------------------------------------------------------------------------------------------------------
print('--- Fazendo busca na árvore AVL ---')
resultados = ['AVL', 0, 0, 0, 0, 0]
for i in range(0, len(chaves_busca)):
    start_time = time.time()
    key = chaves_busca[i].time_low
    pesquisarAVL(root, key)
    tempo_search_avl =  {time.time() - start_time}.pop()
    resultados[(i+1)] = formatNumber(tempo_search_avl)
tempos_busca.append(resultados)
# ------------------------------------------------------------------------------------------------------
# HASH ENCADEAMENTO - INSERT
# Inserir as chaves em uma tabela Hash
# ------------------------------------------------------------------------------------------------------
print('--- Criando e fazendo insert nas Hash Tables ---')
tabelas = []
for qtd in range(10000, 100000, 10000):
    tabela_encadeamento = HashEncadeamento(qtd)
    start_time = time.time()
    for linha in lista_uuid:
        time_low = uuid.UUID(str(linha).replace('\n', '')).time_low
        tabela_encadeamento.insert(time_low, linha)
    total_time = {time.time() - start_time}.pop()
    tabelas.append(tabela_encadeamento)
    tempos_insert.append([qtd, f"{total_time:2f}"])
print(tabulate(tempos_insert))
# ------------------------------------------------------------------------------------------------------
# HASH SEARCH
# Essas chaves estao nas respectivas posições dentro do arquivo de dados:
# posição 200k, 400k, 600k, 800k, 1M
# ------------------------------------------------------------------------------------------------------
print('--- Fazendo a busca das chaves nas Hash Tables ---')
for tabela in tabelas:
    resultados = [tabela.size, 0, 0, 0, 0, 0]
    for i in range(0, len(chaves_busca)):
        start_time = time.time()
        key = chaves_busca[i].time_low
        k, v, j = tabela.search(key)
        tempo_search_chave = {time.time() - start_time}.pop()
        resultados[(i+1)] = formatNumber(tempo_search_chave)
    tempos_busca.append(resultados)

print('--- Fim do processamento e Resultados ---')
print(tabulate(tempos_busca))