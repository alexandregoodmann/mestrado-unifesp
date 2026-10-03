import cv2 #importa biblioteca OpenCV

import numpy as np
from matplotlib import pyplot as grafico

#Carregando e mostrando imagem
imagem = cv2.imread("folha.jpg", 0)
cv2.imshow("Imagem", imagem)

#Histograma com 100 classes
#imagem.ravel() coloca todos os píxeis da imagem em um vetor
grafico.hist(imagem.ravel(), 100, [0,256])
grafico.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

