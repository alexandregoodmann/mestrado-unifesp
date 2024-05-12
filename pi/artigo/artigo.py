# ----------------------------------------------------------------------------------------------------------------
# Aluno: Alexandre Ferreira e Silva
# Atividade 02
#
# Transformacao Afim
# ----------------------------------------------------------------------------------------------------------------

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

import mylib

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')

# Carregar a imagem em tons de cinza
img = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/Screenshot from 2024-05-10 12-17-32.png')
redimensionada = img[::2, ::2]
height, width, r = redimensionada.shape
print('shape', height, width)
imgGray = cv2.cvtColor(redimensionada, cv2.COLOR_BGR2GRAY)

# ---------------------------------------------------------------------------------------------------
# Marca retangulo para poder remover o ruido
# ---------------------------------------------------------------------------------------------------
x0 = 45;
y0 = 35;
xn = x0 + 40;
yn = y0 + 40;
mylib.marcarRetangulo(imgGray, x0, xn, y0, yn, 0)

cv2.imshow('Imagem GrayScale', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------------------------------
# Filtrar imagem e remover fundo
# ---------------------------------------------------------------------------------------------------

# Pega intensidade mínima e máxima para região marcada e adiciona margem 
margem = 20
min = int((imgGray[x0+1:xn-1, y0+1:yn-1].min()) - margem)
max = int(imgGray[x0+1:xn-1, y0+1:yn-1].max() + margem)

imgFiltrada = imgGray
for j in range(0, width):
    for i in range(0, height):
        intensidade = int(imgFiltrada[i,j])
        if (intensidade >= min and intensidade <= max):
            imgFiltrada[i, j] = 255

cv2.imshow('Imagem Filtrada', imgFiltrada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------------------------------
# Converter a imagem para Binario
# ---------------------------------------------------------------------------------------------------
(threshold, imgBinaria) = cv2.threshold(imgFiltrada, 128, 255, cv2.THRESH_BINARY)
print('binaria', threshold, imgBinaria)
cv2.imshow('Imagem Binaria', imgBinaria)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------------------------------
# Marcar celula
# ---------------------------------------------------------------------------------------------------
# Converte binaria para grayscale
imgGray2 = imgBinaria * (255 / imgBinaria.max())
I = mylib.getImagemIntegral(imgGray2)
exit()

imgFiltrada = imgGray
for j in range(0, width):
    for i in range(0, height):
        intensidade = int(imgFiltrada[i,j])
        if (intensidade >= min and intensidade <= max):
            imgFiltrada[i, j] = 255

mylib.marcarRetangulo(imagem_colorida, 0, 13, 0, 13, (0, 255, 0))
cv2.imshow('Imagem Final', imagem_colorida)
cv2.waitKey(0)
cv2.destroyAllWindows()
