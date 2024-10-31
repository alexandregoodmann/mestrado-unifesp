# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Atividade Aula 9
# Fonte: ChatGPT, Google Gemini
# --------------------------------------------------------------------------------------
import os
import time
import random
from tabulate import tabulate # >>>>>> pip install tabulate 
from core import busca_binaria

os.system('cls' if os.name == 'nt' else 'clear')

# ------------------------------------------------------------------------------------------------------
# vetores aleatorios
# ------------------------------------------------------------------------------------------------------
# -- inserção -- 
start_time = time.time()
numeros_aleatorios = [random.randint(0, 10) for _ in range(10)]
tempo_insercao_aleatorio =  {time.time() - start_time}

# -- pesquisa 50 --
start_time = time.time()
for i in (numeros_aleatorios):
    if (i == 50):
        break;
tempo_50_aleatorio =  {time.time() - start_time}

# -- pesquisa 50000 --
start_time = time.time()
for i in (numeros_aleatorios):
    if (i == 50000):
        break;
tempo_50mil_aleatorio =  {time.time() - start_time}

vet_valor_aleatorio = ['Valor aleatorio', tempo_insercao_aleatorio, tempo_50_aleatorio, tempo_50mil_aleatorio]
# ------------------------------------------------------------------------------------------------------
lista_ordenada = []
lista_ordenada.append(numeros_aleatorios[0])

print(numeros_aleatorios, lista_ordenada)


table = [
            ['', 'Tempo insercao', 'Pesquisa 50', 'Pesquisa 50.000'],
            vet_valor_aleatorio
        ]

print(tabulate(table))