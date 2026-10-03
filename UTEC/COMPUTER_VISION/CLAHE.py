import cv2 #importa biblioteca OpenCV

import numpy as np
from matplotlib import pyplot as grafico

#Carregando e mostrando imagem
imagem = cv2.imread("nevoa.jpg", 0)
cv2.imshow("Original", imagem)
#Histograma com da imagem original
grafico.title("Original")
grafico.hist(imagem.ravel(), 256, [0,256], color = "k")
grafico.show()

#Gera imagem com histograma Equalizado (global)
imagemEqua = cv2.equalizeHist(imagem)
cv2.imshow("Imagem Equalizada", imagemEqua)
#Gera seu Histograma
grafico.title("Histograma Equalizado")
grafico.hist(imagemEqua.ravel(), 256, [0,256], color = 'k')
grafico.show()

# Cria um objeto CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
imagemClahe = clahe.apply(imagem)
cv2.imwrite("Clahe.jpg", imagemClahe)
cv2.imshow("Após CLAHE", imagemClahe)
#Mostra histograma da imagem após CLAHE
grafico.title("Após Clahe")
grafico.hist(imagemClahe.ravel(), 256, [0,256], color="k")
grafico.show()


cv2.waitKey(0)
cv2.destroyAllWindows()

