import cv2
import numpy as np
import io
import os
from matplotlib import pyplot as plt

os.system('cls' if os.name == 'nt' else 'clear')

import re

# Carregar a imagem em tons de cinza
img = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/pi/exercicios/Unifesp_secundaria_verde_negativo_RGB.png')
image = img[::2,::2]
verde = [54, 90, 30]
musgo = [79, 71, 55]
w, h, r = image.shape
for i in range(0, w):
    for j in range(0, h):
        if (np.array_equal(image[i,j], verde)):
            image[i,j] = musgo

# Mostrar a imagem original e a imagem binarizada
cv2.imshow('Imagem Original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------------------------------------------------------------------------
# Calcular o histograma da imagem
#--------------------------------------------------------------------------------------
'''
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.plot(histogram)
plt.title('Histograma de Intensidades')
plt.xlabel('Intensidade')
plt.ylabel('Frequência')
plt.show()
'''