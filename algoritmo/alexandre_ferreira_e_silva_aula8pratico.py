# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Atividade Aula 05
# Fonte: ChatGPT, Google Gemini
# --------------------------------------------------------------------------------------
import random
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from core.arvore_avl import inserirAVL, getAlturaEsquerdaAVL, getAlturaDireitaAVL
from core.arvore_binaria import inserirBinaria, pesquisarBinaria

os.system('cls' if os.name == 'nt' else 'clear')

# -----------------------------------------------
# vetores aleatorios
# -----------------------------------------------
# -- inserção -- 
start_time = time.time()
numeros_aleatorios = [random.randint(0, 100000) for _ in range(100000)]
tempo_insercao_aleatorio =  {time.time() - start_time}
# print(f"Tempo inserção aleatórios: {time.time() - start_time} segundos")

# -- pesquisa 50 --
start_time = time.time()
for i in (numeros_aleatorios):
    if (i == 50):
        break;
tempo_50_aleatorio =  {time.time() - start_time}
# print(f"Tempo pesquisa aleatórios 50: {time.time() - start_time} segundos")

# -- pesquisa 50000 --
start_time = time.time()
for i in (numeros_aleatorios):
    if (i == 50000):
        break;
tempo_50mil_aleatorio =  {time.time() - start_time}
#print(f"Tempo pesquisa aleatórios 50000: {time.time() - start_time} segundos")

# -----------------------------------------------
# árvore binária
# -----------------------------------------------
# -- tempo insercao binaria --
start_time = time.time()
root = None
for num in numeros_aleatorios:
    root = inserirBinaria(root, num)
tempo_insercao_binaria =  {time.time() - start_time}

# -- pesquisa 50 --
start_time = time.time()
pesquisarBinaria(root, 50)
tempo_50_binaria =  {time.time() - start_time}

# -- pesquisa 50000 --
start_time = time.time()
pesquisarBinaria(root, 50000)
tempo_50mil_binaria =  {time.time() - start_time}

# -----------------------------------------------
# árvore binária balanceada
# -----------------------------------------------
# -- tempo insercao balanceada --
root = None
start_time = time.time()
for valor in numeros_aleatorios:
    root = inserirAVL(root, valor)
tempo_insercao_balanceada =  {time.time() - start_time}

# -- pesquisa 50 --
start_time = time.time()
pesquisarBinaria(root, 50)
tempo_50_balanceada =  {time.time() - start_time}

# -- pesquisa 50000 --
start_time = time.time()
pesquisarBinaria(root, 50000)
tempo_50mil_balanceada =  {time.time() - start_time}
print("Balanceada: ", tempo_insercao_balanceada, tempo_50_balanceada, tempo_50mil_balanceada)
print("Altura esquerda e direita (AVL): ", getAlturaEsquerdaAVL(root), getAlturaDireitaAVL(root))