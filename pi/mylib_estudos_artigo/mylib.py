import numpy as np
import cv2
from copy import copy

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

# ------------------------------------------------------------------------------------
# Pega intensidade mínima e máxima para uma região aplicando uma margem 
# img[3:6, :] --> Esta notação é do tipo [a,b[, ou seja fechado no início e aberto no final.
# ------------------------------------------------------------------------------------
def getIntensidadeMinMax(img, x0, y0, size, margem):
    xn = x0 + size
    yn = y0 + size
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

def getConvolucao(imgGray, x, y, n):
    return imgGray[x-n:x+n+1, y-n:y+n+1]

def setConvolucao(img, x, y, n, cor):
    img[x-n:x+n+1, y-n:y+n+1] = cor

def getMediaConvolucao(conv):
    h, w = conv.shape
    soma = 0
    for j in range(0, h):
        for i in range(0, w):
            soma = soma + conv[j,i]
    return soma/(h*w)

def procuraCelula(imgFiltrada, n, valor, margem):
    pontos = []
    linhas, colunas = imgFiltrada.shape
    for j in range(n, colunas-n): #colunas
        for i in range(n, linhas-n): #linhas
            conv = getConvolucao(imgFiltrada, i, j, n)
            media = getMediaConvolucao(conv)
            if (media >= valor-margem and media <= valor+margem):
                pontos.append([i,j, media])
    return pontos
# 1 ------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
def varrerImagem(imgBW):
    qtd = 0
    linhas, colunas = imgBW.shape
    for i in range(0, linhas): #linhas
        for j in range(0, colunas): #colunas
            if (imgBW[i,j] == 0):
                qtd = qtd + 1
                removeObjeto(imgBW, i, j)
    return qtd
# 2 ------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
def removeObjeto(imgBW, x, y):
    pontos = []
    pontos.append([x,y])
    imgBW[x, y] = 255
    while (pontos.__len__() > 0):
        P = pontos[0]
        del pontos[0]
        vizinhos = getVizinhos(imgBW, x, y)
        if (vizinhos.__len__() > 0):
            pontos.append(vizinhos)

def getVizinhos(imgBW, x, y):
    vizinhos = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (imgBW[i, j] == 0):
                print('vizinho', i, j)
                imgBW[i,j] = 255
                vizinhos.append(imgBW[i,j])
    return vizinhos
        


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

def detect_edges(image):
    # Converte a imagem para tons de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplica o operador Sobel nos eixos x e y
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=1)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=1)
    
    # Calcula a magnitude do gradiente
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    
    # Normaliza a magnitude para o intervalo [0, 255]
    magnitude = np.uint8(magnitude)
    
    return magnitude

def detect_circles(image):
    # Converte a imagem para tons de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplica um desfoque para reduzir o ruído
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)
    
    # Detecta os círculos usando a transformada de Hough
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                               param1=100, param2=30, minRadius=10, maxRadius=200)
    
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            # Desenha o círculo detectado
            cv2.circle(image, (x, y), r, (0, 255, 0), 4)
    
    return image

def showImage(msg, img):
    cv2.imshow(msg, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    