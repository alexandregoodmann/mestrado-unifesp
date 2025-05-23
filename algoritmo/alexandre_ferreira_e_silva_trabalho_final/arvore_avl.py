# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Fonte: ChatGPT, Google Gemini
# --------------------------------------------------------------------------------------

import random

# Definição da classe de nó para a árvore AVL
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Inicialmente, cada nó tem altura 1

# Função auxiliar para obter a altura de um nó
def obter_altura(node):
    if node is None:
        return 0
    return node.height

# Função para calcular a altura da subárvore esquerda
def getAlturaEsquerdaAVL(node):
    if node is None:
        return 0
    return obter_altura(node.left)

def getAlturaDireitaAVL(node):
    if node is None:
        return 0
    return obter_altura(node.right)

# Função para rotacionar à direita (para balanceamento da AVL)
def rotacionar_direita(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(obter_altura(y.left), obter_altura(y.right))
    x.height = 1 + max(obter_altura(x.left), obter_altura(x.right))
    return x

# Função para rotacionar à esquerda (para balanceamento da AVL)
def rotacionar_esquerda(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(obter_altura(x.left), obter_altura(x.right))
    y.height = 1 + max(obter_altura(y.left), obter_altura(y.right))
    return y

# Função para obter o fator de balanceamento
def fator_balanceamento(node):
    if node is None:
        return 0
    return obter_altura(node.left) - obter_altura(node.right)

# Função para inserir um nó na árvore AVL e manter o balanceamento
def inserirAVL(node, value):
    if node is None:
        return Node(value)
    
    if value < node.value:
        node.left = inserirAVL(node.left, value)
    elif value > node.value:
        node.right = inserirAVL(node.right, value)
    else:
        return node
    
    node.height = 1 + max(obter_altura(node.left), obter_altura(node.right))

    balanceamento = fator_balanceamento(node)

    # Se o nó está desbalanceado, aplicamos rotações para corrigir
    if balanceamento > 1 and value < node.left.value:
        return rotacionar_direita(node)
    
    if balanceamento < -1 and value > node.right.value:
        return rotacionar_esquerda(node)
    
    if balanceamento > 1 and value > node.left.value:
        node.left = rotacionar_esquerda(node.left)
        return rotacionar_direita(node)

    if balanceamento < -1 and value < node.right.value:
        node.right = rotacionar_direita(node.right)
        return rotacionar_esquerda(node)
    
    return node

def pesquisarAVL(root, key):
    if not root:
        return None
    if root.value == key:
        return root
    if key < root.value:
        return pesquisarAVL(root.left, key)
    return pesquisarAVL(root.right, key)