# ----------------------------------------------------------------------------------------------------------------
# Aluno: Alexandre Ferreira e Silva
# Atividade 02
#
# Transformacao Afim
# ----------------------------------------------------------------------------------------------------------------

import numpy as np
import os
from matplotlib import pyplot as plt
import mylib
import cv2
from copy import copy

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')
dir = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/'
fileName = 'sperm_3.png'

# ---------------------------------------------------------------------------------------------------
# Carregar a imagem original
# ---------------------------------------------------------------------------------------------------
def carregarImagem():
    img = cv2.imread(dir + fileName)
    cv2.imshow('Imagem', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img

# ---------------------------------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------------------------------
img = carregarImagem()

# ---------------------------------------------------------------------------------------------------
# Pega intensidade min e max de um retangulo arbitrariamente escolhido
# converte imagem em cinza e marca zona de intensidade para filtro
# ---------------------------------------------------------------------------------------------------
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
min, max = mylib.getIntensidadeMinMax(imgGray, 30, 60, 40, 70, 20)
print('min max da zona filtrada', min, max)
imgMarked = mylib.setBordaQuadrada(1, imgGray, 30, 40, 40, 0)
cv2.imshow('Imagem Gray', imgMarked)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------------------------------
# Filtrar imagem e remover fundo
# ---------------------------------------------------------------------------------------------------
# varre toda a imagem e remove fundo cinza
imgFiltrada = imgGray
width, height = imgGray.shape
for j in range(0, width-1):
    for i in range(0, height-1):
        intensidade = imgFiltrada[j, i]
        if (intensidade >= min and intensidade <= max):
            imgFiltrada[j, i] = 255

cv2.imshow('Imagem Filtrada', imgFiltrada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------------------------------
# Pega a intensidade media de uma celula
# ---------------------------------------------------------------------------------------------------
print(imgGray.shape)
size = 27 #inteiro impar
n = (size-1)/2
x0 = 85
xn = 85 + size
y0 = 10
yn = y0 + size
media = mylib.getIntensidadeMedia(imgGray, x0, xn, y0, yn)

print('media da celula', media)
print('min max da celula', min, max)
imgMarked = mylib.setBordaQuadrada(1, imgMarked, x0, y0, size, 0)
cv2.imshow('Imagem Filtrada', imgMarked)
cv2.waitKey(0)
cv2.destroyAllWindows()

pontos = mylib.procuraCelula(imgFiltrada, int(n), int(media), 5)
print('pontos', pontos)

p = pontos[0]
imgMarked2 = copy(img)
#imgMarked2[98:125,13:40] = (0,0,255)
#imgMarked2[98:125,34:61] = (0,255,0)

for p in pontos:
    #imgMarked2[p[0],p[1]] = (0,255,0)
    mylib.setConvolucao(imgMarked2, p[0], p[1], 5)

cv2.imshow('Imagem Filtrada', imgMarked2)
cv2.waitKey(0)
cv2.destroyAllWindows()