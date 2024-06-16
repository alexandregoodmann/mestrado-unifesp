# --------------------------------------------------------------------------------------
# Aluno: Alexandre Ferreira e Silva
# Atividade 03
#
# Morfologia
# python3 laboratorio3.py '/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio3/letra_A.jpg' 1 5 '/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio3/letra_A_saida.jpg'
# 1-erosão; 2-dilatação; 3-abertura; 4-fechamento.
# --------------------------------------------------------------------------------------

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import sys

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')

# parametros de entrada
'''
arquivo = sys.argv[1]
operacao = sys.argv[2]
tamanho = sys.argv[3]
'''

arquivo = '/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio3/letra_A.jpg'
operacao = 2
tamanho = 5
elemento = []
parte = 1

# Exibe a imagem preto e branco
imgGray = cv2.imread(arquivo, cv2.IMREAD_GRAYSCALE)
'''
imgGray = imgGray[::2, ::2]
cv2.imwrite(arquivo, imgGray)
exit()
'''
(thresh, imgBW) = cv2.threshold(imgGray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
'''
cv2.imshow('Imagem Preto e Branco', imgBW)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# --------------------------------------------------------------------------------------------
# Cria o elemento estruturante com o tamanho de entrada
# --------------------------------------------------------------------------------------------
def getParte():
    parte = 1
    if (tamanho > 3):
        parte = int(tamanho/2)
    return parte
# --------------------------------------------------------------------------------------------
# Cria o elemento estruturante com o tamanho de entrada
# --------------------------------------------------------------------------------------------
def criarElementoEstruturante():
    objeto = np.zeros((tamanho, tamanho))
    return objeto

# --------------------------------------------------------------------------------------------
# Metodo usado para saber se a convolucao esta completamente dentro da imagem
# img - Imagem
# i, j - coordenadas
# d - dimensao da convolucao
# --------------------------------------------------------------------------------------------
def isInside(i, j):
    segmento = imgBW[(i-parte):(i+parte+1), (j-parte):(j+parte+1)]
    return np.array_equal(segmento, elemento)

# --------------------------------------------------------------------------------------------
# EROSAO
# --------------------------------------------------------------------------------------------
def erosao():
    # Cria imagem branca do mesmo tamanho
    imgErosao = np.zeros(imgGray.shape)
    imgErosao[:,:] = 255

    # Com base na imagem original, cria a imagem com erosao
    linhas, colunas = imgBW.shape
    for i in range(parte, linhas-parte):
        for j in range(parte, colunas-parte):
            if (imgBW[i,j] == 0 and isInside(i, j)):
                imgErosao[i,j] = 0
    return imgErosao

# --------------------------------------------------------------------------------------------
# DILATACAO
# --------------------------------------------------------------------------------------------
def dilatacao():
    imgDilatacao = np.copy(imgBW)
    linhas, colunas = imgBW.shape
    for i in range(parte, linhas-parte):
        for j in range(parte, colunas-parte):
            if (imgBW[i,j] == 0 and isInside(i, j) == False):
                imgDilatacao[(i-parte):(i+parte+1), (j-parte):(j+parte+1)] = 0
    return imgDilatacao

# --------------------------------------------------------------------------------------------
# PRINCIPAL
# --------------------------------------------------------------------------------------------  

# Parte foi considerado como a metade do tamanho informado para o elemento estruturante. Sera sempre impar, pois considera o pixel central
parte = getParte()

# Cria elemento estruturante com base no tamanho informado
elemento = criarElementoEstruturante()            

# Aplica a operacao de acordo com numero passado
match operacao:
    case 1:
        imgErosao = erosao()
    case 2:
        imgDilatacao = dilatacao()

plt.subplot(231),plt.imshow(imgBW),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(imgDilatacao),plt.title('DILATACAO')
plt.show()