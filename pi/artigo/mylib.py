import numpy as np

# ------------------------------------------------------------------------------------
# Para calculo da imagem integral, cria-se uma matriz zero, adiciona uma linha e coluna
# Coloca os dados da imagem original dentro dessa matriz zero
# Calcula-se a imagem integral utilizando a formula

# Exemplo de imagem e sua imagem integral
'''
imgIntegral = np.matrix([[5, 8, 1, 2, 9], [10, 8 ,7, 6, 2], [4, 3, 1, 4, 5], [8, 9, 2, 3, 5], [6, 8, 7, 1, 3]])
[[  0.   0.   0.   0.   0.   0.]
 [  0.   5.  13.  14.  16.  25.]
 [  0.  15.  31.  39.  47.  58.]
 [  0.  19.  38.  47.  59.  75.]
 [  0.  27.  55.  66.  81. 102.]
 [  0.  33.  69.  87. 103. 127.]]
'''
# ------------------------------------------------------------------------------------
# Marca em preto um retangulo em uma imagem com base nas coordenadas
# imgMarked = mylib.setQuadrado(img, 3, 3, 3)
# Lembrando que a matriz começa com (0,0), logo o quarto pixel deverá ser (3,3)
# ------------------------------------------------------------------------------------
def setBordaQuadrada(isGray, img, x0, y0, size, color):

    if (isGray==1):
        color = 0
    else:
        h, w, r = img.shape

    xn = x0 + size - 1
    yn = y0 + size - 1
    img[x0, y0:yn] = color
    img[xn, y0:yn] = color
    img[x0:xn, y0] = color
    img[x0:xn, yn] = color
    img[xn, yn] = color
    return img

# ------------------------------------------------------------------------------------
# Pega intensidade mínima e máxima para uma região aplicando uma margem 
# img[3:6, :] --> Esta notação é do tipo [a,b[, ou seja fechado no início e aberto no final.
# ------------------------------------------------------------------------------------
def getIntensidadeMinMax(img, x0, xn, y0, yn, margem):
    min = img[x0:xn, y0:yn].min() - margem
    max = img[x0:xn, y0:yn].max() + margem
    return min, max


def getImagemIntegral(imgGray):
    M, N = imgGray.shape # linhas, colunas
    I = np.zeros((M+1, N+1))
    i = I
    i[1:, 1:] = imgGray

    #calculo de imagem integral
    for x in range(1, M+1): 
        for y in range(1, N+1):
            I[x,y] = i[x,y] + I[x, y-1] + I[x-1, y] - I[x-1, y-1]
    #print(I)
    I = I[1:, 1:]
    return I

# ------------------------------------------------------------------------------------
# Calcular area do retangulo a partir da imagem integral recebendo as coordenadas
# ------------------------------------------------------------------------------------
def getAreaRegangulo(I, x0, xn, y0, yn):
    area = I[xn, yn] - I[x0-1, yn] - I[xn, y0-1] + I[x0-1, y0-1]
    return area

# ------------------------------------------------------------------------------------
# Calcula a média de intensidade de um retângulo a partir da imagem integral
# ------------------------------------------------------------------------------------
def getIntensidadeMedia(imgGray, x0, xn, y0, yn):
    soma = 0
    for j in range(x0, xn):
        for i in range (y0, yn):
            soma = soma + imgGray[j,i]
    return soma/((xn-x0)*(yn-y0))