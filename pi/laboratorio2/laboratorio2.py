# --------------------------------------------------------------------------------------
# Aluno: Alexandre Ferreira e Silva
# Atividade 02
#
# Transformacao Afim
# --------------------------------------------------------------------------------------

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')

# --------------------------------------------------------------------------------------
# Metodo para rotacao no centro da imagem
# --------------------------------------------------------------------------------------
def rotacao_central(imagem, matriz):
    altura, largura, _ = imagem.shape
    centro_x, centro_y = largura / 2, altura / 2

    _0_0 = matriz[0,0]
    _0_1 = matriz[0,1]
    matriz_rotacao = np.array([[_0_0, -_0_1, centro_x * (1 - _0_0) + centro_y * _0_1],
                               [_0_1, _0_0, centro_y * (1 - _0_0) - centro_x * _0_1],
                               [0, 0, 1]])

    transformada = np.zeros_like(imagem)

    for y in range(altura):
        for x in range(largura):
            coords = np.dot(matriz_rotacao, [x, y, 1]).astype(int)
            _x, _y = coords[0], coords[1]

            if 0 <= _x < largura and 0 <= _y < altura:
                transformada[_y, _x] = imagem[y, x]

    return transformada

# --------------------------------------------------------------------------------------
# Metodo para transformacao afim
# --------------------------------------------------------------------------------------
def transformacao_afim(imagem, matriz):
    altura, largura, _ = imagem.shape
    transformada = np.zeros_like(imagem)

    for y in range(altura):
        for x in range(largura):
            coords = np.dot(matriz, [x, y, 1]).astype(int)
            _x, _y = coords[0], coords[1]

            if 0 <= _x < largura and 0 <= _y < altura:
                transformada[_y, _x] = imagem[y, x]

    return transformada

# --------------------------------------------------------------------------------------
# Carrega a imagem em matrizes de transformacao
# --------------------------------------------------------------------------------------

dir = '/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio2/'

imagem = cv2.imread(dir + 'Lenna.png')
mat1_identidade = np.loadtxt(dir + "mat1.txt", delimiter=' ')
mat2_rotacao = np.loadtxt(dir + "mat2.txt", delimiter=' ')
mat3_dilatacao = np.loadtxt(dir + "mat3.txt", delimiter=' ')
mat4_translacao = np.loadtxt(dir + "mat4.txt", delimiter=' ')
mat5_reducao = np.loadtxt(dir + "mat5.txt", delimiter=' ')
mat6_cisalhamento = np.loadtxt(dir + "mat6.txt", delimiter=' ')
mat7_aumento = np.loadtxt(dir + "mat7.txt", delimiter=' ')

# --------------------------------------------------------------------------------------
# A - Rotacao e reducao
# --------------------------------------------------------------------------------------
imagem_rotacao_central = rotacao_central(imagem, mat2_rotacao)
imagem_rotacao_reducao = transformacao_afim(imagem_rotacao_central, mat5_reducao)

print('Matriz de Rotacao\n', mat2_rotacao)
print('Matriz de Reducao\n', mat5_reducao)

plt.subplot(331),plt.imshow(imagem),plt.title('ORIGINAL')
plt.subplot(332),plt.imshow(imagem_rotacao_central),plt.title('ROTACAO')
plt.subplot(333),plt.imshow(imagem_rotacao_reducao),plt.title('REDUCAO')

# --------------------------------------------------------------------------------------
# B - cisalhamento, translacao e rotacao
# --------------------------------------------------------------------------------------
imagem_cisalahmento = transformacao_afim(imagem, mat6_cisalhamento)
imagem_cisalahmento_translacao = transformacao_afim(imagem_cisalahmento, mat4_translacao)
imagem_cisalahmento_translacao_rotacao = rotacao_central(imagem_cisalahmento_translacao, mat2_rotacao)

print('Matriz de Cisalhamento\n', mat6_cisalhamento)
print('Matriz de Translacao\n', mat4_translacao)
print('Matriz de Rotacao\n', mat2_rotacao)

plt.subplot(334),plt.imshow(imagem_cisalahmento),plt.title('CISALHAMENTO')
plt.subplot(335),plt.imshow(imagem_cisalahmento_translacao),plt.title('TRANSLACAO')
plt.subplot(336),plt.imshow(imagem_cisalahmento_translacao_rotacao),plt.title('ROTACAO')

# --------------------------------------------------------------------------------------
# C - rotacao e aumento
# --------------------------------------------------------------------------------------
imagem_rotacao = rotacao_central(imagem, mat2_rotacao)
imagem_rotacao_aumento = transformacao_afim(imagem_rotacao, mat7_aumento)

print('Matriz de Rotacao\n', mat2_rotacao)
print('Matriz de Aumento\n', mat7_aumento)

plt.subplot(337),plt.imshow(imagem_rotacao),plt.title('ROTACAO')
plt.subplot(338),plt.imshow(imagem_rotacao_aumento),plt.title('AUMENTO')

plt.show()