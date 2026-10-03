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
imagem_BGR = cv2.imread('Imagens/baboon.jpg')
imagem_RGB = cv2.cvtColor(imagem_BGR, cv2.COLOR_BGR2RGB)
imagem_HSV = cv2.cvtColor(imagem_BGR, cv2.COLOR_BGR2HSV)
canal_H, canal_S, canal_V = cv2.split(imagem_HSV)

# ---------------------------------------------------------------------------------------------
# Método para adicionar as imagens na visualização
# i - linha
# j - coluna
# img - imagem ou gráfico
# titulo - Rótulo da imagem ou gráfico
# ---------------------------------------------------------------------------------------------
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
    axs[i, j].plot(hist, color='blue')
    axs[i, j].set_title(titulo)
    axs[i, j].set_xlabel('Intensidade de Pixel')
    axs[i, j].set_ylabel('Número de Pixels')

# ---------------------------------------------------------------------------------------------
# Linha 1 - Exibe imagens BGR, RGB e HSV
# ---------------------------------------------------------------------------------------------
fig1, axs = plt.subplots(4, 3, figsize=(15, 15))
addImg(0, 0, imagem_BGR, 'Imagem BGR')
addImg(0, 1, imagem_RGB, 'Imagem RGB')
addImg(0, 2, imagem_HSV, 'Imagem HSV')


# ---------------------------------------------------------------------------------------------
# Linha 2 - Canais Azul, Verde e Vermelho
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
# Linha 4 - Exibir imagem com aplicação de cada canal equalizado
# ---------------------------------------------------------------------------------------------
equa_H = cv2.equalizeHist(canal_H)
equa_S = cv2.equalizeHist(canal_S)
equa_V = cv2.equalizeHist(canal_V)
merge_H = cv2.merge([equa_H, canal_S, canal_V])
merge_S = cv2.merge([canal_H, equa_S, canal_V])
merge_V = cv2.merge([canal_H, canal_S, equa_V])

addImg(3, 0, cv2.cvtColor(merge_H, cv2.COLOR_HSV2RGB), 'Imagem com Azul Equalizado')
addImg(3, 1, cv2.cvtColor(merge_S, cv2.COLOR_HSV2RGB), 'Imagem com Verde Equalizado')
addImg(3, 2, cv2.cvtColor(merge_V, cv2.COLOR_HSV2RGB), 'Imagem com Vermelhor Equalizado')

plt.tight_layout()
plt.show()

# ---------------------------------------------------------------------------------------------
# Salva imagem equalizada e exibe juntamente com original
# ---------------------------------------------------------------------------------------------
cv2.imwrite('entraga_1/baboon_equalizacao_V.jpg', cv2.cvtColor(merge_V, cv2.COLOR_HSV2BGR))
cv2.imshow('BGR', imagem_BGR)
cv2.imshow('Imagem Equalizada Canal V', cv2.cvtColor(merge_V, cv2.COLOR_HSV2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()
