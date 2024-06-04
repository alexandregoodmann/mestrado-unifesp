import numpy as np
import cv2
from copy import copy

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
objetos = []
def contarCelulas(imgBW):
    w, h = imgBW.shape
    for i in range (1, w-1):
        for j in range(1, h-1):
            if (imgBW[i,j] == 0):
                marcados.append([i,j])
                setPixelBlank(imgBW, [i,j])
    return objetos

def setPixelBlank(imgBW, coor):
    vizinhos = []
    vizinhos.append(coor)
    w, h = imgBW.shape
    while (marcados.__len__() > 0):
        x = marcados[0][0]
        y = marcados[0][1]
        imgBW[x,y] = 180
        del marcados[0]
        if ((x+2)<= w and (y+2) <= h):
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if (imgBW[i,j] == 0):
                        imgBW[i,j] = 180
                        vizinhos.append([i,j])
                        marcados.append([i,j])
    objetos.append(vizinhos)