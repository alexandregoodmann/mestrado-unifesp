import numpy as np

# ------------------------------------------------------------------------------------
# Para calculo da imagem integral, cria-se uma matriz zero, adiciona uma linha e coluna
# Coloca os dados da imagem original dentro dessa matriz zero
# Calcula-se a imagem integral utilizando a formula
# ------------------------------------------------------------------------------------
def getImagemIntegral(imgGray):
    M, N = imgGray.shape # linhas, colunas
    I = np.zeros((M+1, N+1))
    i = I
    i[1:, 1:] = imgGray

    #calculo de imagem integral
    for x in range(1, M+1): 
        for y in range(1, N+1):
            I[x,y] = i[x,y] + I[x, y-1] + I[x-1, y] - I[x-1, y-1]

    I = I[1:, 1:]
    return I

# ------------------------------------------------------------------------------------
# Marca em preto um retangulo em uma imagem com base nas coordenadas
# ------------------------------------------------------------------------------------
def marcarRetangulo(img, x0, xn, y0, yn, cor):
    img[x0, y0:yn] = cor
    img[xn, y0:yn] = cor
    img[x0:xn, y0] = cor
    img[x0:xn, yn] = cor

# ------------------------------------------------------------------------------------
# Calcular area do retangulo a partir da imagem integral recebendo as coordenadas
# ------------------------------------------------------------------------------------
def getAreaRegangulo(I, x0, xn, y0, yn):
    area = I[xn, yn] - I[x0-1, yn] - I[xn, y0-1] + I[x0-1, y0-1]
    return area

# ------------------------------------------------------------------------------------
# Calcula a média de intensidade de um retângulo a partir da imagem integral
# ------------------------------------------------------------------------------------
def getMediaIntensidade(I, x0, xn, y0, yn):
    intensidade = I[yn, xn] - I[y0-1, xn] - I[yn, x0-1] + I[y0-1, x0-1]
    num_pixels = (xn - x0 + 1) * (yn - y0 + 1)
    media_intensidade = intensidade / num_pixels
    return media_intensidade