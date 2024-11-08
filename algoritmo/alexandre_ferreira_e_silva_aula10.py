# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Atividade Aula 9
# Fonte: ChatGPT, Google Gemini
# --------------------------------------------------------------------------------------

import os
import math
import time
import random
from tabulate import tabulate # >>>>>> pip install tabulate 
from core.vetor_ordenado import inserir_ordenada, pesquisar_ordenada
from core.arvore_binaria import inserirBinaria, pesquisarBinaria
from core.arvore_avl import inserirAVL, getAlturaEsquerdaAVL, getAlturaDireitaAVL
from core.arvore_vermelho_preto import RedBlackTree

os.system('cls' if os.name == 'nt' else 'clear')

table = [
    ['Valor', 'Calculo', 'Index']
]
vet = [5, 28, 19, 15, 20, 33, 12, 17, 10]
indexx = []
for k in vet:
    k
    #print('h('+str(k)+') = '+ str(k) + ' mod 9 = ' + str(k%9))

vet2 = [61, 62, 63, 64, 35]
A = (math.sqrt(5) - 1)/2
for k in vet2:
    y = 1000*(k*A%1)
    #print('h('+str(k)+') = '+ str(k) + ' mod 1 = ' + str(int(y)))

vet3 = [10, 22, 31, 4, 15, 28, 17, 88, 59]
for k in vet3:
    y = k%11
    print('h('+str(k)+') = '+ str(k) + ' mod 1 = ' + str(int(y)))

'''
h(28) = 28 mod 1 = 6
h(17) = 17 mod 1 = 6
h(88) = 88 mod 1 = 0
h(5) = 5 mod 1 = 5
'''

print(1+2*(28%10))
