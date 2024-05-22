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
fileName = 'sperm_1_reduzido.png'

# ---------------------------------------------------------------------------------------------------
# MAIN
# Pega intensidade min e max de um retangulo arbitrariamente escolhido
# converte imagem em cinza e marca zona de intensidade para filtro
# ---------------------------------------------------------------------------------------------------
# Carrega imagem
img = cv2.imread(dir + fileName)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgMarked = copy(imgGray)
mylib.setBordaQuadrada(1, imgMarked, 50, 25, 40, 0) #marca1
mylib.setBordaQuadrada(1, imgMarked, 23, 21, 15, 0) #marca2

# min max marca1 para usar no filtro
min, max = mylib.getIntensidadeMinMax(imgGray, 50, 25, 40, 20) 
print('min max da zona filtrada', min, max)

media = mylib.getIntensidadeMedia(imgGray, 23, 38, 21, 36)
print('media da celula', media)

cv2.imshow('Imagem Gray', imgMarked)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------------------------------
# Filtrar imagem e remover fundo
# ---------------------------------------------------------------------------------------------------
# varre toda a imagem e remove fundo cinza
width, height = imgGray.shape
for j in range(0, width-1):
    for i in range(0, height-1):
        intensidade = imgGray[j, i]
        if (intensidade >= min and intensidade <= max):
            imgGray[j, i] = 255

cv2.imshow('Imagem Filtrada', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------------------------------
# Pega a intensidade media de uma celula
# ---------------------------------------------------------------------------------------------------

ret, bw_img = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY) 
bw_img = cv2.cvtColor(bw_img, cv2.COLOR_BGR2RGB)
bw_img = cv2.cvtColor(bw_img, cv2.COLOR_BGR2GRAY)
print('shape bw', bw_img.shape)
cv2.imshow("Binary", bw_img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

size = 15 #inteiro impar
n = (size-1)/2

pontos = mylib.procuraCelula(bw_img, int(n), media, 2)
print('pontos', pontos.__len__())

imgMarked2 = cv2.cvtColor(imgGray, cv2.COLOR_BGR2RGB)
for p in pontos:
    mylib.setConvolucao(imgMarked2, p[0], p[1], 1, (0, 255, 0))

cv2.imshow('Imagem Filtrada', imgMarked2)
cv2.waitKey(0)
cv2.destroyAllWindows()