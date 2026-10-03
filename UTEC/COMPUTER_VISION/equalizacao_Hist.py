import cv2 #importa biblioteca OpenCV

import numpy as np
from matplotlib import pyplot as grafico

#Carregando e mostrando imagem
imagemOriginal = cv2.imread("nevoa.jpg", 0)
cv2.imshow("Imagem", imagemOriginal)

#Gera Histograma
grafico.title("Histograma Original")
grafico.hist(imagemOriginal.ravel(), 256, [0,256], color = 'k')
grafico.show()

#Gera imagem com histograma Equalizado
imagemEqua = cv2.equalizeHist(imagemOriginal)
cv2.imshow("Imagem Equalizada", imagemEqua)

#Gera Histograma da nova imagem
grafico.title("Histograma Equalizado")
grafico.hist(imagemEqua.ravel(), 256, [0,256], color = 'k')
grafico.show()

cv2.imwrite("nevoaEqua.jpg", imagemEqua)

cv2.waitKey(0)
cv2.destroyAllWindows()

