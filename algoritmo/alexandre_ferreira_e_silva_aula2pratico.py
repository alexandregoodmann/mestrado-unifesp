# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Atividade Aula 04
# Fonte: Copilot, Desmos
# --------------------------------------------------------------------------------------

import os
import random
import time
import matplotlib.pyplot as plt
from tabulate import tabulate # >>>>>> pip install tabulate 

os.system('cls' if os.name == 'nt' else 'clear')
numeros_aleatorios = [random.randint(0, 100000) for _ in range(100000)]
tempos = [['Algoritmo','Número 9', 'Número 99.999']]

# ------------------------------------------------------------------------------------------------------
# METODO PARA FORMATAR NUMERO
# ------------------------------------------------------------------------------------------------------
def formatNumber(number):
    scaled_number = number * 1e6
    return f"{scaled_number:.4f}"

# -----------------------------------------------
# BUSCA SEQUENCIAL
# -----------------------------------------------
def busca_sequencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# Busca Numero 9
start_time = time.time()
busca_sequencial(numeros_aleatorios, 9)
time_sequencial_9 =  {time.time() - start_time}.pop()

# Busca Numero 99999
start_time = time.time()
busca_sequencial(numeros_aleatorios, 99999)
time_sequencial_99999 =  {time.time() - start_time}.pop()

tempos.append(['Sequencial', formatNumber(time_sequencial_9), formatNumber(time_sequencial_99999)])

# -----------------------------------------------
# BUSCA BINARIA
# -----------------------------------------------
def busca_binaria(lista, elemento):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

# Busca Numero 9
start_time = time.time()
busca_binaria(numeros_aleatorios, 9)
time_binario_9 =  {time.time() - start_time}.pop()

# Busca Numero 99999
start_time = time.time()
busca_binaria(numeros_aleatorios, 99999)
time_binario_99999 =  {time.time() - start_time}.pop()

tempos.append(['Binario', formatNumber(time_binario_9), formatNumber(time_binario_99999)])

# -----------------------------------------------
# RESULTADOS
# -----------------------------------------------
print(tabulate(tempos, stralign="right"))

# -----------------------------------------------
# ANALISE COMPLEXIDADE
# -----------------------------------------------

qtd = []
binaria = []
sequencial = []

for size in range(100, 10000, 100):
    vet = [random.randint(1, size) for _ in range(size)]
    # ----
    init = time.time()
    for a in vet:
        busca_binaria(vet, a)
    endBinaria = time.time() - init
    # ----
    init = time.time()
    for b in vet:
        busca_sequencial(vet, b)
    endSequencial = time.time() - init

    qtd.append(size)
    binaria.append(endBinaria)
    sequencial.append(endSequencial)

# --------------------------------------------------------------------------------------

plt.title("Análise de Complexidade para método Sequencial e Binário")
plt.xlabel("Tamanho do Array")
plt.ylabel("Tempo(s)")
plt.plot(qtd, binaria, color='red')
plt.plot(qtd, sequencial, color='blue')
plt.grid(axis = 'y')
plt.legend(('Binário', 'Sequencial'))
plt.show()
