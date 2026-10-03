# ---------------------------------------------------------------------------------------------
# UTEC - Pós Graduação em Robótica e Inteligência Artificial
# Disciplina: Visão Computacional
# Aluno: Alexandre Ferreira e Silva
# TAREFA 1
# ---------------------------------------------------------------------------------------------

import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
os.system('cls')

# ---------------------------------------------------------------------------------------------
# Carregar Imagem e dividir os canais
# ---------------------------------------------------------------------------------------------
imagem_BGR = cv2.imread('Imagens/apple.jpg')
imagem_RGB = cv2.cvtColor(imagem_BGR, cv2.COLOR_BGR2RGB)
imagem_HSV = cv2.cvtColor(imagem_BGR, cv2.COLOR_BGR2HSV)
canal_H, canal_S, canal_V = cv2.split(imagem_HSV)

# definindo intervalo de cores
inicio = np.array([8, 0, 0])
fim = np.array([20, 255, 255])
img_mask = cv2.inRange(imagem_HSV, inicio, fim)
img_result = cv2.bitwise_and(imagem_HSV, imagem_HSV, mask=img_mask)

# ---------------------------------------------------------------------------------------------
# Método para adicionar as imagens na visualização
# i - linha
# j - coluna
# img - imagem ou gráfico
# titulo - Rótulo da imagem ou gráfico
# ---------------------------------------------------------------------------------------------
fig1, axs = plt.subplots(4, 3, figsize=(12, 12))
def addImg(i, j, img, titulo, gray=False):
    if gray:
        axs[i, j].imshow(img, cmap='gray')
    else:
        axs[i, j].imshow(img)
    axs[i, j].set_title(titulo)
    axs[i, j].axis('off')

# ---------------------------------------------------------------------------------------------
# Método para adicionar Histograma na visualização
# ---------------------------------------------------------------------------------------------
def addHist(i, j, hist, titulo):
    axs[i, j].plot(hist)
    axs[i, j].set_title(titulo)
    axs[i, j].set_xlabel('Intensidade de Pixel')
    axs[i, j].set_ylabel('Número de Pixels')


# ---------------------------------------------------------------------------------------------
# Linha 1 - Imagens em BGR e HSV
# ---------------------------------------------------------------------------------------------
addImg(0, 0, imagem_RGB, 'Imagem Original RGB')
addImg(0, 1, imagem_HSV, 'Imagem HSV')


# ---------------------------------------------------------------------------------------------
# Linha 2 - Canais HSV
# ---------------------------------------------------------------------------------------------
addImg(1, 0, canal_H, 'Canal H', gray=True)
addImg(1, 1, canal_S, 'Canal S', gray=True)
addImg(1, 2, canal_V, 'Canal V', gray=True)

# ---------------------------------------------------------------------------------------------
# Linha 3 - Histograma para cada Canal
# ---------------------------------------------------------------------------------------------
hist_H = cv2.calcHist([canal_H], [0], None, [256], [0, 256])
hist_S = cv2.calcHist([canal_S], [0], None, [256], [0, 256])
hist_V = cv2.calcHist([canal_V], [0], None, [256], [0, 256])

addHist(2, 0, hist_H, 'Histograma H')
addHist(2, 1, hist_S, 'Histograma S')
addHist(2, 2, hist_V, 'Histograma V')

# ---------------------------------------------------------------------------------------------
# Linha 4 - Exibir histograma dos canais equalizados
# ---------------------------------------------------------------------------------------------
addImg(3, 0, imagem_RGB, 'Imagem Original')
addImg(3, 1, img_mask, 'Resultado da segmentação', gray=True)
addImg(3, 2, cv2.cvtColor(img_result, cv2.COLOR_HSV2RGB), 'Máscara Binária')

cv2.imwrite('entraga_1/maca_segmentada.jpg', img_mask)
cv2.imwrite('entraga_1/maca_segmentada2.jpg', img_result)

plt.tight_layout()
plt.show()