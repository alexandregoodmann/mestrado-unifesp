import cv2
import numpy as np
import io
import os
from matplotlib import pyplot as plt
import sys

# limpar console
os.system('cls' if os.name == 'nt' else 'clear')

img = cv2.imread('C:\\projetos\\mestrado-unifesp\\pi\\imgs\\frutas-verduras-e-legumes-da-estacao-no-verao-1-1.png')
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgGray = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2GRAY)

# IMAGEM UNICA -------------------------------------------
'''
cv2.imshow('Imagem Preto e Branco', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# HISTOGRAMA -------------------------------------------
'''
histogram = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histogram)
plt.title('Histograma de Intensidades')
plt.xlabel('Intensidade')
plt.ylabel('Frequência')
plt.show()
'''
# THRESH -------------------------------------------
'''
intensidade = 127
terminal = 255
_, t1 = cv2.threshold(imgGray, intensidade, terminal, cv2.THRESH_BINARY)
#_, t2 = cv2.threshold(imgGray, intensidade, 255, cv2.THRESH_BINARY_INV)
_, t3 = cv2.threshold(imgGray, intensidade, terminal, cv2.THRESH_TRUNC)
#_, t4 = cv2.threshold(imgGray, intensidade, 255, cv2.THRESH_TOZERO)
#_, t5 = cv2.threshold(imgGray, intensidade, 255, cv2.THRESH_TOZERO_INV)

images = [imgRGB, imgGray, t1, t3]

fig = plt.figure()
for i in range(0, len(images)):
    ax = fig.add_subplot(2, 2, i+1)
    ax.imshow(images[i], cmap='gray')
plt.show()
'''

# CANAIS -------------------------------------------
b, g, r = cv2.split(img)
_, t1 = cv2.threshold(g, 7, 255, cv2.THRESH_BINARY)
edges = cv2.Canny(imgGray, 100, 200)
images = [b, g, r, imgRGB, imgGray, t1, edges]

fig = plt.figure()
for i in range(0, len(images)):
    ax = fig.add_subplot(3, 3, i+1)
    ax.imshow(images[i], cmap='gray')
    ax.axis('off')
plt.show()