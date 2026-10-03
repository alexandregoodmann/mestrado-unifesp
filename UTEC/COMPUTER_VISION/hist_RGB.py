import cv2 #importa biblioteca OpenCV

import numpy as np
from matplotlib import pyplot as grafico

#Carregando e mostrando imagem
imagem = cv2.imread("folha.jpg")
cv2.imshow("Imagem", imagem)

#Divide imagem em canais RGB
azul, verde, vermelho = cv2.split(imagem)
cv2.imshow("Canal vermelho", vermelho)
cv2.imshow("Canal verde", verde)
cv2.imshow("Canal azul", azul)

#Histogramas com 256 classes
grafico.title("Azul")
grafico.hist(azul.ravel(), 256, [0,256], color='b')
grafico.figure();

grafico.title("Verde")
grafico.hist(verde.ravel(), 256, [0,256], color='g')
grafico.figure();

grafico.title("Vermelho")
grafico.hist(vermelho.ravel(), 256, [0,256], color='r')
grafico.show();

cv2.waitKey(0)
cv2.destroyAllWindows()

