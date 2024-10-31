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
from alexandre_ferreira_e_silva_aula8pratico_2 import Node, avl_inserir, avl_altura_esquerda, avl_altura_direita

os.system('cls' if os.name == 'nt' else 'clear')

# --------------------------------------------------------------------------------------
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right) if root else []

def buscar(root, key):
    if not root:
        return None
    if root.value == key:
        return root
    if key < root.value:
        return buscar(root.left, key)
    return buscar(root.right, key)

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    
    for num in reversed(arr): 
        output[count[num] - 1] = num
        count[num] -= 1
    
    for i in range(len(arr)):
        arr[i] = output[i]

def altura_esquerda_binaria(node):
    if node is None:
        return 0
    altura = 0
    atual = node.left  # Focando apenas no lado esquerdo
    while atual is not None:
        altura += 1
        atual = atual.left  # Desce pela subárvore esquerda
    return altura

def altura_direita_binaria(node):
    if node is None:
        return 0
    altura = 0
    atual = node.right  # Focando apenas no lado direito
    while atual is not None:
        altura += 1
        atual = atual.right  # Desce pela subárvore direita
    return altura

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
print("Aleatórios: ", tempo_insercao_aleatorio, tempo_50_aleatorio, tempo_50mil_aleatorio)

# -----------------------------------------------
# árvore binária
# -----------------------------------------------
# -- tempo insercao binaria --
start_time = time.time()
root = None
for num in numeros_aleatorios:
    root = insert(root, num)
tempo_insercao_binaria =  {time.time() - start_time}

# -- pesquisa 50 --
start_time = time.time()
buscar(root, 50)
tempo_50_binaria =  {time.time() - start_time}

# -- pesquisa 50000 --
start_time = time.time()
buscar(root, 50000)
tempo_50mil_binaria =  {time.time() - start_time}
print("Binária:    ", tempo_insercao_binaria, tempo_50_binaria, tempo_50mil_binaria)
print("Altura esquerda e direita (Binária): ", altura_esquerda_binaria(root), altura_direita_binaria(root))

# -----------------------------------------------
# árvore binária balanceada
# -----------------------------------------------
# -- tempo insercao balanceada --
root = None
start_time = time.time()
for valor in numeros_aleatorios:
    root = avl_inserir(root, valor)
tempo_insercao_balanceada =  {time.time() - start_time}

# -- pesquisa 50 --
start_time = time.time()
buscar(root, 50)
tempo_50_balanceada =  {time.time() - start_time}

# -- pesquisa 50000 --
start_time = time.time()
buscar(root, 50000)
tempo_50mil_balanceada =  {time.time() - start_time}
print("Balanceada: ", tempo_insercao_balanceada, tempo_50_balanceada, tempo_50mil_balanceada)
print("Altura esquerda e direita (AVL): ", avl_altura_esquerda(root), avl_altura_direita(root))