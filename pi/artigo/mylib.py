import numpy as np
import cv2
from copy import copy
from typing import Final
from matplotlib import pyplot as plt

# ------------------------------------------------------------------------------------
# Constantes
# ------------------------------------------------------------------------------------
TAMANHO_MIN_CELULA: Final = 60
TAMANHO_MAXIMO_CELULA: Final = 108
INTENSIDADE_CELULA_MARCADA: Final = 180
INTENSIDADE_GRUPO: Final = 80

# ------------------------------------------------------------------------------------
# Marca em preto um retangulo em uma imagem com base nas coordenadas
# imgMarked = mylib.setQuadrado(img, 3, 3, 3)
# Lembrando que a matriz começa com (0,0), logo o quarto pixel deverá ser (3,3)
# ------------------------------------------------------------------------------------
def setBordaQuadrada(isGray, img, x0, y0, size, color):

    if (isGray==1):
        color = 0
    else:
        h, w, r = img.shape

    xn = x0 + size - 1
    yn = y0 + size - 1
    img[x0, y0:yn] = color
    img[xn, y0:yn] = color
    img[x0:xn, y0] = color
    img[x0:xn, yn] = color
    img[xn, yn] = color

# ------------------------------------------------------------------------------------
# Pega intensidade mínima e máxima para uma região aplicando uma margem 
# img[3:6, :] --> Esta notação é do tipo [a,b[, ou seja fechado no início e aberto no final.
# ------------------------------------------------------------------------------------
def getIntensidadeMinMax(img, x0, y0, size, margem):
    xn = x0 + size
    yn = y0 + size
    min = img[x0:xn, y0:yn].min() - margem
    max = img[x0:xn, y0:yn].max() + margem
    return min, max

# ------------------------------------------------------------------------------------------
# Contagem das celulas
# ------------------------------------------------------------------------------------------
marcados = []
celulas = []
grupos = []
def contarCelulas(imgBW):
    w, h = imgBW.shape
    for i in range (1, w-1):
        for j in range(1, h-1):
            if (imgBW[i,j] == 0):
                marcados.append([i,j])
                __setPixelBlank(imgBW, [i,j])
    agrupadas = __calcularCelulasAgrupadas(imgBW)
    qtd = celulas.__len__() + agrupadas
    return qtd, imgBW, celulas, grupos

def __setPixelBlank(imgBW, coor):
    item = []
    item.append(coor)
    w, h = imgBW.shape
    while (marcados.__len__() > 0):
        x = marcados[0][0]
        y = marcados[0][1]
        imgBW[x,y] = INTENSIDADE_CELULA_MARCADA
        del marcados[0]
        if ((x+2)<= w and (y+2) <= h):
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if (imgBW[i,j] == 0):
                        imgBW[i,j] = INTENSIDADE_CELULA_MARCADA
                        item.append([i,j])
                        marcados.append([i,j])
    if (item.__len__() >= TAMANHO_MIN_CELULA and item.__len__() <= TAMANHO_MAXIMO_CELULA):
        celulas.append(item)
    if (item.__len__() > TAMANHO_MAXIMO_CELULA):
        grupos.append(item)

def __calcularCelulasAgrupadas(imgBW):
    qtd = 0
    for grupo in grupos:
        qtd += int(grupo.__len__()/TAMANHO_MIN_CELULA)
        for coordenada in grupo:
            imgBW[coordenada[0], coordenada[1]] = INTENSIDADE_GRUPO
    return qtd

# ------------------------------------------------------------------------------------------
# Cortar imagem de 3 canais
# Parametros: imagem, fatiar linhas, fatilar colunas
# ------------------------------------------------------------------------------------------
def cortarImagem(img, linhas, colunas):
    partes = []
    largura, altura, canais = img.shape
    passo_a = int(largura/colunas)
    passo_b = int(altura/linhas)
    for i in range(0, largura, passo_a):
        for j in range(0, altura, passo_b):
            partes.append(img[i:i+passo_a, j:j+passo_b])
    return partes

# ------------------------------------------------------------------------------------------
# Converte imagem para binario
# ------------------------------------------------------------------------------------------
def converterBinario(imgGray, T):
    imgBW = copy(imgGray)
    width, height = imgBW.shape
    for i in range(0, width):
        for j in range(0, height):
            if (imgGray[i,j] <= T):
                imgBW[i,j] = 0
            else:
                imgBW[i,j] = 255
    return imgBW