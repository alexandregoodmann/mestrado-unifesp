import numpy as np
import cv2
from copy import copy
import os

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')

#---------------------------------------------------------
# Metodos para varrer imagem e contar o numero de pontos
#---------------------------------------------------------
marcados = []
def varrerImagem():
    w, h = imgBW.shape
    obj = 0
    for i in range (1, w-1):
        for j in range(1, h-1):
            if (imgBW[i,j] == 0):
                marcados.append([i,j])
                setPixelBlank()
                obj += 1
    return obj

def setPixelBlank():
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
                        marcados.append([i,j])

#---------------------------------------------------------
# main
#---------------------------------------------------------
path2 = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/teste01.png'
path3 = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/istockphoto-1188380375-1024x1024.jpg'
imgGray = cv2.imread(path3, cv2.IMREAD_GRAYSCALE)
#imgGray = cv2.resize(imgGray, (0, 0), fx = 0.75, fy = 0.75)
(thresh, imgBW) = cv2.threshold(imgGray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('shape', imgBW.shape)
obj= varrerImagem()
print('objetos', obj)
cv2.imshow('imagem teste', imgBW)
cv2.waitKey(0)
cv2.destroyAllWindows()