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
from hash_encadeamento import HashEncadeamento
from arvore_avl import inserirAVL, pesquisarAVL
from tabulate import tabulate # >>>>>> pip install tabulate 
os.system('cls' if os.name == 'nt' else 'clear')

import uuid

# ------------------------------------------------------------------------------------------------------
# ABRIR MASSA DE DADOS
# Arquivo com 296 mil registros
# ------------------------------------------------------------------------------------------------------
linhas = []
buscas = []
with open("trabalho_final\Emendas-Parlamentares.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=";")
    for qtd, linha in enumerate(arquivo_csv):
        key = uuid.uuid1(int(linha[9]))
        linhas.append(key)
        if (qtd % 60000 == 0):
            buscas.append(key)
# ------------------------------------------------------------------------------------------------------
# HASH ENCADEAMENTO
# Inserir as chaves em uma tabela Hash
# ------------------------------------------------------------------------------------------------------
tempos_insert = [
            ['Tamanho', 'Tempo(s)']
         ]
tabelas = []
for qtd in range(10000, 100000, 10000):
    tabela_encadeamento = HashEncadeamento(qtd)
    start_time = time.time()
    for linha in linhas:
        time_low = uuid.UUID(str(linha).replace('\n', '')).time_low
        tabela_encadeamento.insert(time_low, linha)
    total_time =  {time.time() - start_time}
    tabelas.append(tabela_encadeamento)
    #tabela.append(tabela_encadeamento)
    tempos_insert.append([qtd, total_time])

print(tabulate(tempos_insert))

# ------------------------------------------------------------------------------------------------------
# HASH SEARCH
# Essas chaves estao nas respectivas posições dentro do arquivo de dados:
# posição 200k, 400k, 600k, 800k, 1M
# ------------------------------------------------------------------------------------------------------
def format_to_e_minus_6(number):
    scaled_number = number / 1e-6  # Escala para e-06
    return f"{scaled_number:.4f}e-06"

tempos_busca = [
            ['Tamanho', 'Chave 1', 'Chave 2', 'Chave 3', 'Chave 4', 'Chave 5']
         ]
for tabela in tabelas:
    resultados = [tabela.size, 0, 0, 0, 0, 0]
    for i in range(0, len(buscas)):
        start_time = time.time()
        key = buscas[i].time_low
        k, v, j = tabela.search(key)
        tempo_search_chave = {time.time() - start_time}.pop()
        resultados[(i+1)] = format_to_e_minus_6(tempo_search_chave)
    tempos_busca.append(resultados)
print(tabulate(tempos_busca))