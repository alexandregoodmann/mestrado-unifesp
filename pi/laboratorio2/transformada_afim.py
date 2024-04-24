import cv2
import numpy as np
import numpy as np
import os

os.system('cls' if os.name == 'nt' else 'clear')

# Carrega a imagem
imagem = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio2/imgs/Lenna.png')

mat1 = np.loadtxt("/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio2/mat1.txt", delimiter=' ')
mat2 = np.loadtxt("/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio2/mat2.txt", delimiter=' ')
mat3 = np.loadtxt("/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio2/mat3.txt", delimiter=' ')
mat4 = np.loadtxt("/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio2/mat4.txt", delimiter=' ')
print(mat1, mat2)

pontos_origem = np.float32(mat1)
pontos_destino = np.float32([[10, 100], [200, 50], [100, 250]])

transformada = cv2.getAffineTransform(pontos_origem, pontos_destino)
imagem_transformada = cv2.warpAffine(imagem, transformada, (imagem.shape[1], imagem.shape[0]))
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Transformada', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()