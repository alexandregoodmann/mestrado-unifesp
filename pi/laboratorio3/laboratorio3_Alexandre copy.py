# --------------------------------------------------------------------------------------
# Aluno: Alexandre Ferreira e Silva
# Atividade 03
#
# Morfologia
# python3 laboratorio3.py '/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio3/muros.png' 1 5 '/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio3/muros_saida.png'
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
operacao = int(sys.argv[2])
tamanho = int(sys.argv[3])
arquivo_saida = sys.argv[4]
'''
elemento = []
parte = 1

arquivo = '/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio3/muros.png'
arquivo_saida = '/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio3/muros_saida.png'
operacao = 4
tamanho = 5

# Exibe a imagem preto e branco
imgGray = cv2.imread(arquivo, cv2.IMREAD_GRAYSCALE)
(thresh, imgBW) = cv2.threshold(imgGray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('Imagem Preto e Branco', imgBW)
cv2.waitKey(0)
cv2.destroyAllWindows()

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
def isInside(imagem, i, j):
    segmento = imagem[(i-parte):(i+parte+1), (j-parte):(j+parte+1)]
    return np.array_equal(segmento, elemento)

# --------------------------------------------------------------------------------------------
# EROSAO
# --------------------------------------------------------------------------------------------
def erosao(imagem):

    # Cria imagem branca do mesmo tamanho
    linhas, colunas = imagem.shape
    imgErosao = np.zeros((linhas, colunas))
    imgErosao[:,:] = 255

    # Com base na imagem original, cria a imagem com erosao
    for i in range(parte, linhas-parte):
        for j in range(parte, colunas-parte):
            if (imagem[i,j] == 0 and isInside(imagem, i, j)):
                imgErosao[i,j] = 0
    return imgErosao

# --------------------------------------------------------------------------------------------
# DILATACAO
# --------------------------------------------------------------------------------------------
def dilatacao(imagem):
    imgDilatacao = np.copy(imagem)
    linhas, colunas = imagem.shape
    for i in range(parte, linhas-parte):
        for j in range(parte, colunas-parte):
            if (imagem[i,j] == 0 and isInside(imagem, i, j) == False):
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
        imgSaida = erosao(imgBW)
    case 2:
        imgSaida = dilatacao(imgBW)
    case 3:
        imgErosao = erosao(imgBW)
        imgSaida = dilatacao(imgErosao)
    case 4:
        imgDilatacao = dilatacao(imgBW)
        imgSaida = erosao(imgDilatacao)

# Salva a imagem processada
cv2.imwrite(arquivo_saida, imgSaida)

cv2.imshow('Imagem Saida', imgSaida)
cv2.waitKey(0)
cv2.destroyAllWindows()

ero = erosao(imgBW)
dila = dilatacao(imgBW)
abertura = dilatacao(ero)
fechamento = erosao(dila)

plt.subplot(151),plt.imshow(imgBW, cmap='gray'),plt.title('Oritinal')
plt.subplot(152),plt.imshow(ero, cmap='gray'),plt.title('Erosao')
plt.subplot(153),plt.imshow(dila, cmap='gray'),plt.title('Dilatacao')
plt.subplot(154),plt.imshow(abertura, cmap='gray'),plt.title('Abertura')
plt.subplot(155),plt.imshow(fechamento, cmap='gray'),plt.title('Fechamento')
plt.show()