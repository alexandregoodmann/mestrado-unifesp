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

x = np.array([500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000])
y = np.array([0.01216268539428711, 0.057749271392822266, 0.11443877220153809, 0.19830060005187988, 0.3090684413909912, 0.44097042083740234, 0.6098847389221191, 0.7863748073577881, 0.9751787185668945, 1.2147576808929443, 1.4706034660339355, 1.743863582611084, 1.9338898658752441, 2.2849390506744385, 2.630723476409912, 2.9543228149414062, 3.8837218284606934, 3.8149631023406982, 4.235697984695435, 4.854998588562012])
z = np.array([0.0001819133758544922, 0.0003695487976074219, 0.0004551410675048828, 0.0006296634674072266, 0.0007531642913818359, 0.0009083747863769531, 0.0011107921600341797, 0.0011985301971435547, 0.0013420581817626953, 0.0015339851379394531, 0.001619100570678711, 0.0017371177673339844, 0.0019371509552001953, 0.002044200897216797, 0.0022013187408447266, 0.0023686885833740234, 0.002645730972290039, 0.0028200149536132812, 0.0029296875, 0.003327608108520508])

plt.title("CockTail vs Counting")
plt.xlabel("Tamanho do Array")
plt.ylabel("Tempo(s)")

plt.plot(qtd, cock, color='red')
plt.plot(qtd, count, color='blue')

plt.grid(axis = 'y')

plt.show()