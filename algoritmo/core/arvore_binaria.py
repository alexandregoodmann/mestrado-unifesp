# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Fonte: ChatGPT, Google Gemini
# --------------------------------------------------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Inicialmente, cada nó tem altura 1

def inserirBinaria(root, key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = inserirBinaria(root.left, key)
    else:
        root.right = inserirBinaria(root.right, key)
    return root

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right) if root else []

def pesquisarBinaria(root, key):
    if not root:
        return None
    if root.value == key:
        return root
    if key < root.value:
        return pesquisarBinaria(root.left, key)
    return pesquisarBinaria(root.right, key)

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
    atual = node.left  
    while atual is not None:
        altura += 1
        atual = atual.left  
    return altura

def altura_direita_binaria(node):
    if node is None:
        return 0
    altura = 0
    atual = node.right 
    while atual is not None:
        altura += 1
        atual = atual.right 
    return altura