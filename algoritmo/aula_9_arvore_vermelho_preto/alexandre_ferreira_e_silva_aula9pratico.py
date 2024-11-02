# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Atividade Aula 9
# Fonte: ChatGPT, Google Gemini
# Obs.: Caso ocorra exception ao buscar os números 50 e 50000, 
#       rodar o algorítmo algumas vezes pois os números são gerados randomicamente
# --------------------------------------------------------------------------------------
import os
import time
import random
from tabulate import tabulate # >>>>>> pip install tabulate 
from core import inserir, pesquisar

os.system('cls' if os.name == 'nt' else 'clear')

# ------------------------------------------------------------------------------------------------------
# VETOR ALEATORIO
# ------------------------------------------------------------------------------------------------------
# -- inserção -- 
start_time = time.time()
numeros_aleatorios = [random.randint(0, 100000) for _ in range(100000)]
tempo_insercao_aleatorio =  {time.time() - start_time}

# -- pesquisa 50 --
start_time = time.time()
for i in (numeros_aleatorios):
    if (i == 50):
        break
tempo_50_aleatorio =  {time.time() - start_time}

# -- pesquisa 50000 --
start_time = time.time()
for i in (numeros_aleatorios):
    if (i == 50000):
        break
tempo_50mil_aleatorio =  {time.time() - start_time}

vet_valor_aleatorio = ['Vetor aleatorio', tempo_insercao_aleatorio, tempo_50_aleatorio, tempo_50mil_aleatorio]

# ------------------------------------------------------------------------------------------------------
# VETOR ORDENADO
# ------------------------------------------------------------------------------------------------------
# -- inserção -- 
vetor_ordenado = []
start_time = time.time()
for item in numeros_aleatorios:
    inserir(vetor_ordenado, item)
tempo_insert_ordenado =  {time.time() - start_time}

# -- pesquisa 50 --
start_time = time.time()
index = pesquisar(vetor_ordenado, 50)
if (index == -1):
    raise Exception('Nao encontrou 50')
tempo_50_ordenado =  {time.time() - start_time}

# -- pesquisa 50000 --
start_time = time.time()
index = pesquisar(vetor_ordenado, 50000)
if (index == -1):
    raise Exception('Nao encontrou 50000')
tempo_50mil_ordenado =  {time.time() - start_time}

vet_valor_ordenado = ['Vetor ordenado', tempo_insert_ordenado, tempo_50_ordenado, tempo_50mil_ordenado]
# ------------------------------------------------------------------------------------------------------
# RESULTADOS
# ------------------------------------------------------------------------------------------------------
table = [
            ['', 'Tempo insercao', 'Pesquisa 50', 'Pesquisa 50.000'],
            vet_valor_aleatorio,
            vet_valor_ordenado
        ]
print(tabulate(table))