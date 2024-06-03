import os
import cv2

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')

# ------------------------------------------------------------------
# Abrir imagem original
# ------------------------------------------------------------------
path = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo_contar_celulas/imgs/Screenshot from 2024-05-10 12-17-32.png'
img = cv2.imread(path)
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------------------------------------------------------
# Reduzir imagem original a metade e converter em grayscale
# ------------------------------------------------------------------
img = img[::2, ::2]
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Marcar zona para aplicar filtro
mylib.setBordaQuadrada(1, imgMarked, 50, 25, 40, 0) #marca1