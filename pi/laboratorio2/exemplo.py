import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio2/imgs/Lenna.png')

# Pontos de origem e destino para a transformada afim
pontos_origem = np.float32([[50, 50], [200, 50], [50, 200]])
pontos_destino = np.float32([[10, 100], [200, 50], [100, 250]])

# Calcular a matriz de transformação afim
matriz_transformacao = cv2.getAffineTransform(pontos_origem, pontos_destino)

# Aplicar a transformação afim na imagem
imagem_transformada = cv2.warpAffine(imagem, matriz_transformacao, (imagem.shape[1], imagem.shape[0]))

# Mostrar a imagem original e a imagem transformada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Transformada', imagem_transformada)
cv2.waitKey(0)
cv2.destroyAllWindows()
