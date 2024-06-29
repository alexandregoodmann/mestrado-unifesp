import os
import cv2
import mylib
from copy import copy
from matplotlib import pyplot as plt
import numpy as np

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')

# ------------------------------------------------------------------------------------------
# Abrir imagem original
# ------------------------------------------------------------------------------------------
n = 6
path = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/partes/parte_' + str(n) + '.png'
#path = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/imagem_reduzida.png'
quadrados = [[50,  25, 40],
             [50,  85, 40],
             [20,  100,40],
             [80,  80, 40],
             [140, 20, 40],
             [24, 270, 40]]
q = quadrados[n-1]

img = cv2.imread(path)
imgGray = cv2.cvtColor(img[::2,::2], cv2.COLOR_BGR2GRAY)
imgMarcado = copy(imgGray)
mylib.setBordaQuadrada(1, imgMarcado, q[0], q[1], q[2], 0) #marca1

# ------------------------------------------------------------------------------------------
# Filtrar Imagem
# Pega intensidade minima e maxima para o quadrado marcado considerando margem de erro
# Remove todos os pixel com base na nas intensidades
# Transforma a imagem em Binaria 
# ------------------------------------------------------------------------------------------
MIN, MAX = mylib.getIntensidadeMinMax(imgGray, q[0], q[1], q[2], 30) 
print('Mínimo e Máximo de intensidade da zona filtrada:', MIN, MAX)

# varre toda a imagem e remove fundo cinza
imgFiltrado = copy(imgGray)
width, height = imgFiltrado.shape
for j in range(0, width-1):
    for i in range(0, height-1):
        intensidade = imgFiltrado[j, i]
        if (intensidade >= MIN and intensidade <= MAX):
            imgFiltrado[j, i] = 255

# ------------------------------------------------------------------------------------------
# Converte imagem para binario
# ------------------------------------------------------------------------------------------
imgBW = mylib.converterBinario(imgFiltrado, MIN)

# ------------------------------------------------------------------------------------------
# Contagem das celulas
# ------------------------------------------------------------------------------------------
qtd, imgBW, celulas, grupos = mylib.contarCelulas(imgBW)

# ------------------------------------------------------------------------------------------
# Análise numérica das células e grupo
# Definição de tamanho para uso na contagem de células
# ------------------------------------------------------------------------------------------
arrayCelulas = []
for c in celulas:
    arrayCelulas.append(c.__len__())

arrayCelulas = sorted(arrayCelulas)
print('Quantidade de Celulas Únicas:', celulas.__len__())
print('Tamanho das Células Únicas:', arrayCelulas)
print('Quantidade de Grupo:', grupos.__len__())
print('Numero de celulas encontradas:', qtd)

# ------------------------------------------------------------------------------------------
# Plotar Histograma das Células Únicas
# ------------------------------------------------------------------------------------------
'''
# Criar o histograma
plt.hist(arrayCelulas, bins=30, color='blue', alpha=0.7)
plt.title('Histograma Células Únicas')
plt.xlabel('Pixels')
plt.ylabel('Ocorrências')
plt.show()
exit()
'''

plt.subplot(221),plt.imshow(img),plt.title('ORIGINAL')
plt.subplot(222),plt.imshow(imgMarcado, cmap='gray'),plt.title('MARCADO')
plt.subplot(223),plt.imshow(imgFiltrado, cmap='gray'),plt.title('FILTRADO')
plt.subplot(224),plt.imshow(imgBW, cmap='gray'),plt.title('CONTAGEM - ' + str(qtd))
plt.show()