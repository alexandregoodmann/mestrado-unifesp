#Bibliotecas básicas e baixando imagem de teste.
import cv2
import numpy as np
import io
import os
from matplotlib import pyplot as plt

os.system('cls' if os.name == 'nt' else 'clear')

# Carregar a imagem em tons de cinza
image = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/pi/imgs/Lenna.png', cv2.IMREAD_GRAYSCALE)

altura, largura = image.shape
for linha in range(0, largura):
    for coluna in range(0, altura):

print('largura', image.shape)

# Calcular o histograma da imagem
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Calcular o limite de iluminação usando o método de Otsu
_, thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print('Iluminação', _)
# Mostrar a imagem original e a imagem binarizada
cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem Binarizada', thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Plotar o histograma
plt.plot(histogram)
plt.title('Histograma de Intensidades')
plt.xlabel('Intensidade')
plt.ylabel('Frequência')
plt.show()
