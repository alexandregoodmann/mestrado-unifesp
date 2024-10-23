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

os.system('cls' if os.name == 'nt' else 'clear')

# --------------------------------------------------------------------------------------
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

def buscar(root, key):
    if not root:
        return None
    if root.val == key:
        return root
    if key < root.val:
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

class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data

def altura(node):
    if node is None:
        return -1
    else:
        altura_esquerda = altura(node.left)

        altura_direita = altura(node.right)

        return 1 + max(altura_esquerda, altura_direita)
# -----------------------------------------------
# vetores aleatorios
# -----------------------------------------------
qtd = 10**5
# -- inserção -- 
start_time = time.time()
numeros_aleatorios = [random.randint(0, qtd) for _ in range(qtd)]
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
# vetor ordenado + binario
# -----------------------------------------------
'''
vetor_ordenado = numeros_aleatorios.copy()
counting_sort(vetor_ordenado)

# -- tempo insercao binaria --
start_time = time.time()
ordenado = None
for num in vetor_ordenado:
    ordenado = insert(ordenado, num)
tempo_insercao_ordenado =  {time.time() - start_time}

# -- pesquisa 50 --
start_time = time.time()
buscar(ordenado, 50)
tempo_50_ordenado =  {time.time() - start_time}

# -- pesquisa 50000 --
start_time = time.time()
buscar(ordenado, 50000)
tempo_50mil_ordenado =  {time.time() - start_time}
print("Ordenado:    ", tempo_insercao_ordenado, tempo_50_ordenado, tempo_50mil_ordenado)
'''
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

# -- altura --
print(root._len__())
#print(altura(root))
# -----------------------------------------------
# árvore binária balanceada
# -----------------------------------------------
def sorted_array_to_bst(arr):
    if not arr:
        return None

    # Escolher o elemento do meio para ser a raiz
    mid = len(arr) // 2
    root = Node(arr[mid])

    # Recursivamente construir a subárvore esquerda e direita
    root.left = sorted_array_to_bst(arr[:mid])  # Metade esquerda
    root.right = sorted_array_to_bst(arr[mid+1:])  # Metade direita

    return root

# -- tempo insercao balanceada --
start_time = time.time()
root = sorted_array_to_bst(numeros_aleatorios)
tempo_insercao_balanceada =  {time.time() - start_time}

# -- pesquisa 50 --
start_time = time.time()
buscar(root, 50)
tempo_50_balanceada =  {time.time() - start_time}

# -- pesquisa 50000 --
start_time = time.time()
buscar(root, 50000)
tempo_50mil_balanceada =  {time.time() - start_time}
print("Balanceada: ", tempo_insercao_balanceada, tempo_50_balanceada, tempo_50mil_balanceada);