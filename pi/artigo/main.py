import os
import cv2
import mylib
from copy import copy

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')

# ------------------------------------------------------------------------------------------
# Abrir imagem original
# ------------------------------------------------------------------------------------------
path = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/Screenshot from 2024-05-10 12-17-32.png'
img = cv2.imread(path)
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------------------------------------------------------------------------------
# Reduzir imagem original pela metade
# Converter em grayscale
# Marcar zona para aplicar filtragem
# ------------------------------------------------------------------------------------------
img = img[::2, ::2]
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGrayMarked = copy(imgGray)
mylib.setBordaQuadrada(1, imgGrayMarked, 50, 25, 40, 0) #marca1
cv2.imshow('Grayscale', imgGrayMarked)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------------------------------------------------------------------------------
# Pega intensidade minima e maxima para o quadrado marcado considerando margem de erro
# Remove todos os pixel com base na nas intensidades
# ------------------------------------------------------------------------------------------

min, max = mylib.getIntensidadeMinMax(imgGray, 50, 25, 40, 20) 
print('min max da zona filtrada', min, max)

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

# ------------------------------------------------------------------------------------------
# Converte imagem para binario
# ------------------------------------------------------------------------------------------
(thresh, imgBW) = cv2.threshold(imgGray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('Imagem Binaria', imgBW)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------------------------------------------------------------------------------
# Contagem das celulas
# ------------------------------------------------------------------------------------------
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

celulas = varrerImagem()
print('Numero de celulas encontradas', celulas)
cv2.imshow('Imagem Marcada', imgBW)
cv2.waitKey(0)
cv2.destroyAllWindows()