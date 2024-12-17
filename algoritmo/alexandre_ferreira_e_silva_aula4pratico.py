# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Atividade Aula 04
# Fonte: ChatGPT
# --------------------------------------------------------------------------------------

import os
import random
import time
from tabulate import tabulate # >>>>>> pip install tabulate 

os.system('cls' if os.name == 'nt' else 'clear')
numeros_aleatorios = [random.randint(0, 900) for _ in range(900)]
tempos = [['Algoritmo','Crescente', 'Decrescente']]
# -----------------------------------------------
# SHELL SORT
# -----------------------------------------------
def shell_sort(arr, order="asc"):
    fator = 6
    n = len(arr)
    gap = n // fator
    print(gap)

    # Escolhe a função de comparação com base na ordem desejada
    if order == "asc":
        compare = lambda x, y: x > y  # Crescente
    elif order == "desc":
        compare = lambda x, y: x < y  # Decrescente
    else:
        raise ValueError("O parâmetro 'order' deve ser 'asc' ou 'desc'.")

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Modifica a comparação com base na ordem
            while j >= gap and compare(arr[j - gap], temp):
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= fator

    return arr

# Ordenação crescente
start_time = time.time()
quick_asc = shell_sort(numeros_aleatorios, order="asc")
time_shellsort_asc =  {time.time() - start_time}.pop()

# Ordenação decrescente
start_time = time.time()
quick_desc = shell_sort(numeros_aleatorios, order="desc")
time_shellsort_desc =  {time.time() - start_time}.pop()

tempos.append(['ShellSort', time_shellsort_asc, time_shellsort_desc])

# -----------------------------------------------
# HEAPSORT
# -----------------------------------------------
def heapify(arr, n, i, order="asc"):

    if order == "asc":
        compare = lambda x, y: x < y  # Para crescente (max-heap)
    elif order == "desc":
        compare = lambda x, y: x > y  # Para decrescente (min-heap)
    else:
        raise ValueError("O parâmetro 'order' deve ser 'asc' ou 'desc'.")

    largest = i  # Inicializa a raiz como o maior
    left = 2 * i + 1  # Filho esquerdo
    right = 2 * i + 2  # Filho direito

    # Verifica se o filho esquerdo é maior/menor que a raiz
    if left < n and compare(arr[largest], arr[left]):
        largest = left

    # Verifica se o filho direito é maior/menor que o maior atual
    if right < n and compare(arr[largest], arr[right]):
        largest = right

    # Se a raiz não for o maior/menor, troca e ajusta o heap
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca
        heapify(arr, n, largest, order)


def heapsort(arr, order="asc"):
    n = len(arr)

    # Constrói o heap (max-heap para asc, min-heap para desc)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, order)

    # Extrai os elementos do heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move a raiz para o final
        heapify(arr, i, 0, order)

    return arr

# Ordenação crescente
start_time = time.time()
quick_asc = heapsort(numeros_aleatorios.copy(), order="asc")
time_heapsort_asc =  {time.time() - start_time}.pop()

# Ordenação decrescente
start_time = time.time()
quick_desc = heapsort(numeros_aleatorios.copy(), order="desc")
time_heapsort_desc =  {time.time() - start_time}.pop()

tempos.append(['HeapSort', time_heapsort_asc, time_heapsort_desc])

# -----------------------------------------------
# QUICKSORT
# -----------------------------------------------
def quicksort(arr, low, high, order="asc"):
    if low < high:
        # Particiona a lista e obtém o índice do pivô
        pi = partition(arr, low, high, order)

        # Ordena os elementos antes e depois da partição
        quicksort(arr, low, pi - 1, order)
        quicksort(arr, pi + 1, high, order)


def partition(arr, low, high, order="asc"):
    pivot = arr[high]  # Escolhe o último elemento como pivô

    # Define a função de comparação com base na ordem
    if order == "asc":
        compare = lambda x, y: x <= y  # Crescente
    elif order == "desc":
        compare = lambda x, y: x >= y  # Decrescente
    else:
        raise ValueError("O parâmetro 'order' deve ser 'asc' ou 'desc'.")

    i = low - 1  # Índice do menor elemento

    for j in range(low, high):
        # Compara elementos com o pivô
        if compare(arr[j], pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Troca elementos

    # Coloca o pivô na posição correta
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Ordenação crescente
quick_asc = numeros_aleatorios.copy()
start_time = time.time()
quicksort(quick_asc, 0, len(quick_asc) - 5, order="asc")
time_quick_asc =  {time.time() - start_time}.pop()

# Ordenação decrescente
quick_desc = numeros_aleatorios.copy()
start_time = time.time()
quicksort(quick_desc, 0, len(quick_desc) - 5, order="desc")
time_quick_desc =  {time.time() - start_time}.pop()

tempos.append(['QuickSort', time_quick_asc, time_quick_desc])

# -----------------------------------------------
# MERGESORT
# -----------------------------------------------

def merge_sort(arr, order="asc"):
    if len(arr) > 1:
        # Divide a lista em duas metades
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Ordena recursivamente as metades
        merge_sort(left_half, order)
        merge_sort(right_half, order)

        # Combina as duas metades ordenadas
        merge(arr, left_half, right_half, order)


def merge(arr, left_half, right_half, order="asc"):
    i = j = k = 0

    # Define a função de comparação com base na ordem
    if order == "asc":
        compare = lambda x, y: x <= y  # Crescente
    elif order == "desc":
        compare = lambda x, y: x >= y  # Decrescente
    else:
        raise ValueError("O parâmetro 'order' deve ser 'asc' ou 'desc'.")

    # Combina as duas metades comparando os elementos
    while i < len(left_half) and j < len(right_half):
        if compare(left_half[i], right_half[j]):
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Adiciona os elementos restantes da metade esquerda
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Adiciona os elementos restantes da metade direita
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


# Ordenação crescente
sorted_asc = numeros_aleatorios.copy()
start_time = time.time()
merge_sort(sorted_asc, order="asc")
time_merge_asc =  {time.time() - start_time}.pop()

# Ordenação decrescente
sorted_desc = numeros_aleatorios.copy()
start_time = time.time()
merge_sort(sorted_desc, order="desc")
time_merge_desc =  {time.time() - start_time}.pop()

tempos.append(['MergeSort', time_quick_asc, time_quick_desc])

# -----------------------------------------------
# RESULTADOS
# -----------------------------------------------
print(tabulate(tempos))
