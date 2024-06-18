# --------------------------------------------------------------------------------------
# Aluno: Alexandre Ferreira e Silva
# Atividade 03
#
# Morfologia - para rodar o arquivo copiar a linha abaixo e mudar o diretorio
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
arquivo = sys.argv[1]
operacao = int(sys.argv[2])
tamanho = int(sys.argv[3])
arquivo_saida = sys.argv[4]
elemento = []

# Exibe a imagem preto e branco
imgGray = cv2.imread(arquivo, cv2.IMREAD_GRAYSCALE)
(thresh, imgBW) = cv2.threshold(imgGray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('Imagem Preto e Branco', imgBW)
cv2.waitKey(0)
cv2.destroyAllWindows()

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
    parte = int(tamanho/2)
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
    parte = int(tamanho/2)
    for i in range(parte, linhas-parte):
        for j in range(parte, colunas-parte):
            if (imagem[i,j] == 0 and isInside(imagem, i, j)):
                imgErosao[i,j] = 0
    return imgErosao

# --------------------------------------------------------------------------------------------
# DILATACAO
# --------------------------------------------------------------------------------------------
def dilatacao(imagem):
    parte = int(tamanho/2)
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