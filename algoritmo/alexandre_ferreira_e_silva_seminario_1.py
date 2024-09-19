# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Atividade Aula 05
# --------------------------------------------------------------------------------------
import random
import os
import time
import numpy as np
import matplotlib.pyplot as plt

os.system('cls' if os.name == 'nt' else 'clear')

# --------------------------------------------------------------------------------------

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Percorre da esquerda para a direita
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Se nada foi trocado, a lista está ordenada
        if not swapped:
            break

        # Resetar a flag para a próxima etapa
        swapped = False
        # Reduzir o final da lista
        end -= 1

        # Percorre da direita para a esquerda
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Aumentar o início da lista
        start += 1

# --------------------------------------------------------------------------------------
def counting_sort(arr):
    # Encontrar o valor máximo na lista
    max_val = max(arr)
    
    # Inicializar o array de contagem com zeros
    count = [0] * (max_val + 1)
    
    # Armazenar a contagem de cada valor na lista original
    for num in arr:
        count[num] += 1
    
    # Modificar o array de contagem para armazenar as posições acumuladas
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Criar um array de saída para armazenar o resultado ordenado
    output = [0] * len(arr)
    
    # Colocar os elementos em suas posições corretas no array de saída
    for num in reversed(arr):  # Reverso para garantir a estabilidade
        output[count[num] - 1] = num
        count[num] -= 1
    
    # Copiar o array ordenado de volta para o original
    for i in range(len(arr)):
        arr[i] = output[i]
# --------------------------------------------------------------------------------------
qtd = []
cock = []
count = []

for i in range(500, 10500, 500):
    lista = [random.randint(1, i) for _ in range(i)]
    # ----
    cocktail_time_init = time.time()
    cocktail_sort(lista)
    cocktail_time = time.time() - cocktail_time_init
    # ----
    counting_time_init = time.time()
    counting_sort(lista)
    counting_time = time.time() - counting_time_init

    qtd.append(i)
    cock.append(cocktail_time)
    count.append(counting_time)

    print(i, cocktail_time, counting_time)

# --------------------------------------------------------------------------------------

plt.title("CockTail vs Counting")
plt.xlabel("Tamanho do Array")
plt.ylabel("Tempo(s)")
plt.plot(qtd, cock, color='red')
plt.plot(qtd, count, color='blue')
plt.grid(axis = 'y')
plt.show()