import os
import cv2
import mylib
from copy import copy
from matplotlib import pyplot as plt
import numpy as np

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')

# ------------------------------------------------------------------------------------------
# Abrir imagem original
# ------------------------------------------------------------------------------------------
path = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/seccao_1_BW_nao_aglomeradas.jpg'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
img = mylib.converterBinario(img, 128)

qtd, img, celulas, grupos = mylib.contarCelulas(img)

# ------------------------------------------------------------------------------------------
# Análise numérica das células e grupo
# Definição de tamanho para uso na contagem de células
# ------------------------------------------------------------------------------------------
arrayCelulas = []
for c in celulas:
    arrayCelulas.append(c.__len__())

arrayCelulas = sorted(arrayCelulas)
print('Quantidade de Celulas Únicas:', celulas.__len__())
print('Tamanho das Células Únicas:', arrayCelulas)
print('Quantidade de Grupo:', grupos.__len__())
print('Numero de celulas encontradas:', qtd)

# Criar o histograma
plt.hist(arrayCelulas, bins=30, color='blue', alpha=0.7)
plt.title('Histograma Células Únicas')
plt.xlabel('Pixels')
plt.ylabel('Ocorrências')
plt.show()
exit()

cv2.imshow('Source Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()