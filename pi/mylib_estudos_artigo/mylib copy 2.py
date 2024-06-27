import numpy as np
import cv2
from copy import copy
import os

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')

#---------------------------------------------------------
# Metodos
#---------------------------------------------------------
marcados = []
def varrerImagem():
    obj = 0
    print('shape', imgBW.shape)
    w, h = imgBW.shape
    for i in range (1, w-1):
        for j in range(1, h-1):
            if (imgBW[i,j] == 0):
                marcados.append([i,j])
                setPixelBlank()
                obj += 1
    return obj

def setPixelBlank():
    while (marcados.__len__() > 0):
        x = marcados[0][0]
        y = marcados[0][1]
        imgBW[x,y] = 255
        del marcados[0]
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (imgBW[i,j] == 0):
                    imgBW[i,j] = 255
                    marcados.append([i,j])

#---------------------------------------------------------
# main
#---------------------------------------------------------
path1 = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/quadrado_prova.png'
path2 = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/teste01.png'
imgGray = cv2.imread(path2, cv2.IMREAD_GRAYSCALE)
(thresh, imgBW) = cv2.threshold(imgGray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(thresh, imgBW, imgBW.shape)
obj= varrerImagem()
print('objetos', obj)
cv2.imshow('imagem teste', imgBW)
cv2.waitKey(0)
cv2.destroyAllWindows()

