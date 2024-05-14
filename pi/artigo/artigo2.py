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
dir = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/'
img = cv2.imread(dir + 'sperm_3.png')
#redimensionada = img[::2, ::2]
height, width, r = img.shape
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem Gray', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# usado para validar a media
print(imgGray.shape)
print(imgGray[13,13])
soma = 0
for j in range(0,24):
    for i in range(0, 24):
        soma = soma + imgGray[j,i]

media = soma/(25*25)
print('media', media)
I = mylib.getImagemIntegral(imgGray)
media2 = mylib.getIntensidadeMedia(I, 1, 25, 1, 25)
print('media2', media2)
'''

# ---------------------------------------------------------------------------------------------------
# Marca retangulo para poder remover o ruido
# ---------------------------------------------------------------------------------------------------
x0 = 45;
y0 = 35;
xn = x0 + 40;
yn = y0 + 40;
'''
mylib.setRetangulo(imgGray, x0, xn, y0, yn, 0)
cv2.imshow('Imagem GrayScale', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# ---------------------------------------------------------------------------------------------------
# Filtrar imagem e remover fundo
# ---------------------------------------------------------------------------------------------------

# Pega intensidade mínima e máxima
min, max = mylib.getIntensidadeMinMax(imgGray, x0, xn, y0, yn, 20)

# varre toda a imagem e remove fundo cinza
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
#(threshold, imgBinaria) = cv2.threshold(imgFiltrada, 128, 255, cv2.THRESH_BINARY)
#print('binaria', threshold, imgBinaria)
'''
binaria = imgGray
for j in range(0,height):
    for i in range(0, width):
        if (binaria[j,i] < 175):
            binaria[j,i] = 0
cv2.imshow('Imagem Binaria', binaria)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# ---------------------------------------------------------------------------------------------------
# Pega a intensidade media para depois varrer a imagem
# ---------------------------------------------------------------------------------------------------

fit = 23
I = mylib.getImagemIntegral(imgFiltrada)
'''
x1 = 86
x2 = x1 + fit
y1 = 12
y2 = y1 + fit

imedia = mylib.getIntensidadeMedia(I, x1, x2, y1, y2)
print('imedia', imedia)
# imedia = 255
mylib.setRetangulo(imgFiltrada, x1, x2, y1, y2, 0)
'''

cv2.imshow('Imagem Filtrada', imgFiltrada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------------------------------
# Buscar celula
# ---------------------------------------------------------------------------------------------------

coordenadas = []
for j in range(0, width-1): #coluna
    for i in range(0, height-1): #linha
        if (j < (width-fit) and i < (height-fit)):
            x1 = j
            x2 = x1 + fit
            y1 = i
            y2 = y1 + fit
            i_media = mylib.getIntensidadeMedia(I, x1, x2, y1, y2)
            if (i_media == 255):
                coordenadas.append([j,i])

print('coordenadas', coordenadas)