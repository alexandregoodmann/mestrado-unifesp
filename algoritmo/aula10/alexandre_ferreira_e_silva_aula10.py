# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Atividade Aula 9
# Fonte: ChatGPT, Google Gemini
# --------------------------------------------------------------------------------------

import os
import math
import time
import random
from tabulate import tabulate # >>>>>> pip install tabulate 
from hash_encadeamento import HashEncadeamento
from hash_sondagem_linear import HashSondagemLinear
os.system('cls' if os.name == 'nt' else 'clear')

# ------------------------------------------------------------------------------------------------------
# VETOR ALEATORIO
# ------------------------------------------------------------------------------------------------------
numeros_aleatorios = [random.randint(0, 100000) for _ in range(100000)]

# ------------------------------------------------------------------------------------------------------
# HASH ENCADEAMENTO
# ------------------------------------------------------------------------------------------------------
# -- insercao
tabela_encadeamento = HashEncadeamento(50000)
start_time = time.time()
for valor in numeros_aleatorios:
    tabela_encadeamento.insert(valor, valor)
tempo_insercao_encadeamento =  {time.time() - start_time}

# -- busca
start_time = time.time()
tabela_encadeamento.search(10000)
tempo_busca_encadeamento =  {time.time() - start_time}

# ------------------------------------------------------------------------------------------------------
# HASH SONDAGEM LINEAR
# ------------------------------------------------------------------------------------------------------
# -- insercao
tabela_sondagem = HashEncadeamento(100000)
start_time = time.time()
for valor in numeros_aleatorios:
    tabela_sondagem.insert(valor, valor)
tempo_insercao_sondagem =  {time.time() - start_time}

# -- busca
start_time = time.time()
tabela_sondagem.search(10000)
tempo_busca_sondagem =  {time.time() - start_time}

# ------------------------------------------------------------------------------------------------------
# RESULTADOS
# ------------------------------------------------------------------------------------------------------
table = [['','Hash por encadeamento', 'Hash por endereçamento aberto'],
         ['Inserção', tempo_insercao_encadeamento, tempo_insercao_sondagem],
         ['Busca', tempo_busca_encadeamento, tempo_busca_sondagem]   
            ]
print(tabulate(table))