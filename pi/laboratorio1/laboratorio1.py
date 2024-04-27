import cv2
import numpy as np
import io
import os
from matplotlib import pyplot as plt

# limpar console
os.system('cls' if os.name == 'nt' else 'clear')

# Carregar a imagem em tons de cinza
img = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio1/Lenna.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem Preto e Branco', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#imagem para teste
#img = np.matrix([[5, 8, 1, 2, 9], [10, 8 ,7, 6, 2], [4, 3, 1, 4, 5], [8, 9, 2, 3, 5], [6, 8, 7, 1, 3]])

# ------------------------------------------------------------------------------------
# Para calculo da imagem integral, cria-se uma matriz zero, adiciona uma linha e coluna
# Coloca os dados da imagem original dentro dessa matriz zero
# Calcula-se a imagem integral utilizando a formula
# ------------------------------------------------------------------------------------
M, N = imgGray.shape # linhas, colunas
I = np.zeros((M+1, N+1))
i = I
i[1:, 1:] = imgGray

#calculo de imagem integral
for x in range(1, M+1): 
    for y in range(1, N+1):
        I[x,y] = i[x,y] + I[x, y-1] + I[x-1, y] - I[x-1, y-1]

I = I[1:, 1:]
print('Imagem Integral: ', I)

# ------------------------------------------------------------------------------------
# Calcular area do retangulo
# ------------------------------------------------------------------------------------
x0 = 200
xn = 300
y0 = 250
yn = 300
area = I[xn, yn] - I[x0-1, yn] - I[xn, y0-1] + I[x0-1, y0-1]
print('Area do retangulo: ', area)

# ------------------------------------------------------------------------------------
# Media de intensidade
# ------------------------------------------------------------------------------------
intensidade = I[yn, xn] - I[y0-1, xn] - I[yn, x0-1] + I[y0-1, x0-1]
num_pixels = (xn - x0 + 1) * (yn - y0 + 1)
media_intensidade = intensidade / num_pixels
print("Média da intensidade: ", media_intensidade)

# ------------------------------------------------------------------------------------
# Exibir imagem colorida com borda
# ------------------------------------------------------------------------------------
imgColor = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2RGB)
imgColor[x0, y0:yn] = (0, 0, 255)
imgColor[xn, y0:yn] = (0, 0, 255)
imgColor[x0:xn, y0] = (0, 0, 255)
imgColor[x0:xn, yn] = (0, 0, 255)
cv2.imshow('Imagem com borda', imgColor)
cv2.waitKey(0)
cv2.destroyAllWindows()