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
dir = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/'
fileName = 'sperm_3.png'

# ----------------------------------------------------------------------------------------------------------------
# Carregar a imagem original
# ----------------------------------------------------------------------------------------------------------------
def carregarImagem():
    img = cv2.imread(dir + fileName)
    cv2.imshow('Imagem', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img

# ----------------------------------------------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------------------------------------------
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
imgMarked = mylib.setBordaQuadrada(1, imgMarked, 85, 10, 30, 0)

print('min max da celula', min, max)
cv2.imshow('Imagem Filtrada', imgMarked)
cv2.waitKey(0)
cv2.destroyAllWindows()