import cv2
import numpy as np

def calcular_imagem_integral(imagem):
    # Converte a imagem para escala de cinza
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Calcula a imagem integral
    integral_image = cv2.integral(imagem_gray)
    
    return integral_image

# Carrega a imagem
imagem = cv2.imread('/home/alexandre/Documents/PI/imgs/Lenna.png')

# Calcula a imagem integral
integral = calcular_imagem_integral(imagem)

cv2.imshow('Imagem Integral', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Exibe a imagem integral
cv2.imshow('Imagem Integral', integral.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
