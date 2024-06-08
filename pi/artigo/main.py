import os
import cv2
import mylib
from copy import copy
from matplotlib import pyplot as plt

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')

# ------------------------------------------------------------------------------------------
# Abrir imagem original
# ------------------------------------------------------------------------------------------
path = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/Screenshot from 2024-05-10 12-17-32.png'
path1 = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/seccao_1_BW_nao_aglomeradas.jpg'

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
print(img.shape)
img = img[0:184, 0:275]
cv2.imwrite('/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/seccao_1.jpg', img)
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
#imgBW = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/seccao_1_BW.jpg', cv2.IMREAD_GRAYSCALE)
(thresh, imgBW) = cv2.threshold(imgGray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#cv2.imwrite('/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/seccao_1_BW.jpg', imgBW)
cv2.imshow('Imagem Binaria', imgBW)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------------------------------------------------------------------------------
# Contagem das celulas
# ------------------------------------------------------------------------------------------
celulas = mylib.contarCelulas(imgBW)
print('Numero de celulas encontradas', celulas.__len__())
cv2.imshow('Imagem Marcada', imgBW)
cv2.waitKey(0)
cv2.destroyAllWindows()

# imprimir lado a lado
'''
plt.subplot(221),plt.imshow(img),plt.title('ORIGINAL')
plt.subplot(222),plt.imshow(imgGrayMarked),plt.title('MARCADO')
plt.subplot(223),plt.imshow(imgGray),plt.title('FILTRADO')
plt.subplot(224),plt.imshow(imgBW),plt.title('BW - ' + str(celulas))
plt.show()
'''