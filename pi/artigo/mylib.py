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

