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
from core.vetor_ordenado import inserir_ordenada, pesquisar_ordenada
from core.arvore_binaria import inserirBinaria, pesquisarBinaria
from core.arvore_avl import inserirAVL

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

tempos_vetor_aleatorio = ['Vetor Aleatório', tempo_insercao_aleatorio, tempo_50_aleatorio, tempo_50mil_aleatorio]

# ------------------------------------------------------------------------------------------------------
# VETOR ORDENADO
# ------------------------------------------------------------------------------------------------------
# -- inserção -- 
vetor_ordenado = []
start_time = time.time()
for item in numeros_aleatorios:
    inserir_ordenada(vetor_ordenado, item)
tempo_insert_ordenado =  {time.time() - start_time}

# -- pesquisa 50 --
start_time = time.time()
index = pesquisar_ordenada(vetor_ordenado, 50)
tempo_50_ordenado =  {time.time() - start_time}

# -- pesquisa 50000 --
start_time = time.time()
index = pesquisar_ordenada(vetor_ordenado, 50000)
tempo_50mil_ordenado =  {time.time() - start_time}

tempos_vetor_ordenado = ['Vetor Ordenado', tempo_insert_ordenado, tempo_50_ordenado, tempo_50mil_ordenado]

# ------------------------------------------------------------------------------------------------------
# ÁRVORE BINÁRIA
# ------------------------------------------------------------------------------------------------------
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

tempos_arvore_binaria = ['Árvore Binária', tempo_insercao_binaria, tempo_50_binaria, tempo_50mil_binaria]

# -----------------------------------------------
# ÁRVORE BINÁRIA AVL
# -----------------------------------------------
# -- tempo insercao balanceada --
root = None
start_time = time.time()
for valor in numeros_aleatorios:
    root = inserirAVL(root, valor)
tempo_insercao_avl =  {time.time() - start_time}

# -- pesquisa 50 --
start_time = time.time()
pesquisarBinaria(root, 50)
tempo_50_avl =  {time.time() - start_time}

# -- pesquisa 50000 --
start_time = time.time()
pesquisarBinaria(root, 50000)
tempo_50mil_avl =  {time.time() - start_time}

tempos_arvore_avl = ['Árvore AVL', tempo_insercao_avl, tempo_50_avl, tempo_50mil_avl]

# ------------------------------------------------------------------------------------------------------
# RESULTADOS
# ------------------------------------------------------------------------------------------------------
table = [
            ['', 'Tempo Inserção', 'Pesquisa 50', 'Pesquisa 50000'],
            tempos_vetor_aleatorio,
            tempos_vetor_ordenado,
            tempos_arvore_binaria,
            tempos_arvore_avl
        ]
print(tabulate(table))