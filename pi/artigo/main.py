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
#path = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/imagem_reduzida.png'
path = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/seccao_1.jpg'
contagem = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/seccao_1_counted.jpg'

img = cv2.imread(path)
imgContagem = cv2.imread(contagem)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgMarcado = copy(imgGray)
mylib.setBordaQuadrada(1, imgMarcado, 50, 25, 40, 0) #marca1

# ------------------------------------------------------------------------------------------
# Filtrar Imagem
# Pega intensidade minima e maxima para o quadrado marcado considerando margem de erro
# Remove todos os pixel com base na nas intensidades
# Transforma a imagem em Binaria 
# ------------------------------------------------------------------------------------------
MIN, MAX = mylib.getIntensidadeMinMax(imgGray, 50, 25, 40, 20) 
print('min max da zona filtrada', MIN, MAX)

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
imgBW = mylib.converterBinario(imgFiltrado, 162)

# ------------------------------------------------------------------------------------------
# Contagem das celulas
# ------------------------------------------------------------------------------------------
celula = copy(imgBW)
celulas = mylib.contarCelulas(celula)
print('Numero de celulas encontradas', celulas)

plt.subplot(231),plt.imshow(img),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(imgContagem),plt.title('CONTAGEM')
plt.subplot(234),plt.imshow(imgMarcado, cmap='gray'),plt.title('MARCADO')
plt.subplot(235),plt.imshow(imgFiltrado, cmap='gray'),plt.title('FILTRADO')
plt.subplot(236),plt.imshow(imgBW, cmap='gray'),plt.title('CONTAGEM - ' + str(celulas))
plt.show()