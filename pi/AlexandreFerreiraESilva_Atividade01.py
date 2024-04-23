# --------------------------------------------------------------------------------------
# Aluno: Alexandre Ferreira e Silva
# Atividade 01
#
# Para rodar digitar como no comando abaixo:
# python3 AlexandreFerreiraESilva_Atividade01.py '/home/alexandre/Documents/PI/imgs/Lenna.png' 10 50 20 70
# --------------------------------------------------------------------------------------

import cv2 as cv
import sys

# --------------------------------------------------------------------------------------
# Abrir imagem colorida e exibir em escala de cinza
# --------------------------------------------------------------------------------------
imagem_gray = cv.imread(sys.argv[1], cv.IMREAD_GRAYSCALE)
cv.imshow('Source Image', imagem_gray)
cv.waitKey(0)
cv.destroyAllWindows()

# --------------------------------------------------------------------------------------
# Abrir imagem em escala de cinza com retangulo colorido a partir das coordenadas de entrada
# --------------------------------------------------------------------------------------
x0 = int(sys.argv[2])
xn = int(sys.argv[3])
y0 = int(sys.argv[4])
yn = int(sys.argv[5])

imagem_color = cv.cvtColor(imagem_gray, cv.COLOR_GRAY2RGB)
imagem_color[x0, y0:yn] = (255, 0, 0)
imagem_color[xn, y0:yn] = (0, 255, 0)
imagem_color[x0:xn, y0] = (0, 0, 255)
imagem_color[x0:xn, yn] = (255, 255, 255)

cv.imshow('Source Image', imagem_color)
cv.waitKey(0)
cv.destroyAllWindows()

# --------------------------------------------------------------------------------------
# Calculo da imagem integral
# --------------------------------------------------------------------------------------
altura, largura, canais = imagem_color.shape
imagem_integral = [[0] * largura for _ in range(altura)]
for y in range(altura):
    for x in range(largura):
        if y == 0:
            imagem_integral[y][x] = imagem_color[y][x]
        else:
            imagem_integral[y][x] = imagem_integral[y-1][x] + imagem_color[y][x]

area = imagem_integral[yn][xn] - imagem_integral[yn][x0-1] - imagem_integral[y0-1][xn] + imagem_integral[y0-1][x0-1]
media = area // ((xn - x0 + 1) * (yn - y0 + 1))
print("Area:", area)
print("Coordenadas:", x0, y0, xn, yn)
print("Media:", media)
exit()