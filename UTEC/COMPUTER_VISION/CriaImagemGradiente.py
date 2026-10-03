import numpy as np
import cv2 as cv

# Define o tamanho da imagem que será criada
n = 100  # Número de linhas
m = 100  # Número de colunas

# Defini o incremento para gerar o gradiente
r = 255/(m-1)

# Cria a image (matrix) do tamanho desenjado (escala de cinza)
img = np.empty((n,m),np.uint8)

# Percorre os pixels da matriz atribuindo o valor calculado
for i in range(0, n):
    for j in range(0,m):
        img[i][j] = j*r

# Escreve a imagem
cv.imwrite("gradiente.png",img )
