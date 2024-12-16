# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Atividade Aula 01
# Fonte: ChatGPT, Desmos Grphic Calculator
# --------------------------------------------------------------------------------------

import os
import random
import math
import time
import matplotlib.pyplot as plt
from tabulate import tabulate # >>>>>> pip install tabulate 

os.system('cls' if os.name == 'nt' else 'clear')
numeros_aleatorios = [random.randint(0, 1000) for _ in range(1000)]
tempos = [['','Recursivo', 'Iterativo'],
          ['Número Primo', 0, 0],
          ['Tempo', 0, 0]
          ]

# -----------------------------------------------
# RECURSIVO
# -----------------------------------------------
def isPrimoRecursivo(numero, divisor=None):
    if numero < 2:
        return False
    
    if divisor is None:
        divisor = numero - 1
    
    if divisor == 1:
        return True
    
    if numero % divisor == 0:
        return False
    
    return isPrimoRecursivo(numero, divisor - 1)

start_time = time.time()
maiorRecursivo = 0
for size in numeros_aleatorios:
    if (isPrimoRecursivo(size) and size > maiorRecursivo):
        maiorRecursivo = size
end_time =  {time.time() - start_time}.pop()

tempos[1][1] = maiorRecursivo
tempos[2][1] = end_time

# -----------------------------------------------
# ITERATIVO
# -----------------------------------------------
def isPrimoIterativo(numero):
    if numero < 2:
        return False
    
    for divisor in range(2, int(math.sqrt(numero)) + 1):
        if numero % divisor == 0:
            return False  
    
    return True  

start_time = time.time()
maiorIterativo = 0
for size in numeros_aleatorios:
    if (isPrimoIterativo(size) and size > maiorIterativo):
        maiorIterativo = size
end_time =  {time.time() - start_time}.pop()

tempos[1][2] = maiorIterativo
tempos[2][2] = end_time

# -----------------------------------------------
# RESULTADOS
# -----------------------------------------------
print(tabulate(tempos))

# -----------------------------------------------
# ANALISE COMPLEXIDADE
# -----------------------------------------------

qtd = []
recursivo = []
iterativo = []

for size in range(10, 1000, 10):
    vet = [random.randint(1, size) for _ in range(size)]
    # ----
    init = time.time()
    for a in vet:
        isPrimoRecursivo(a)
    endRecursivo = time.time() - init
    # ----
    init = time.time()
    for b in vet:
        isPrimoIterativo(b)
    endIterativo = time.time() - init

    qtd.append(size)
    recursivo.append(endRecursivo)
    iterativo.append(endIterativo)

    #print(size, endRecursivo, endIterativo)

# --------------------------------------------------------------------------------------

plt.title("Análise de Complexidade para método Recursivo e Iterativo")
plt.xlabel("Tamanho do Array")
plt.ylabel("Tempo(s)")
plt.plot(qtd, recursivo, color='red')
plt.plot(qtd, iterativo, color='blue')
plt.grid(axis = 'y')
plt.legend(('Recursivo', 'Iterativo'))
plt.show()

# 