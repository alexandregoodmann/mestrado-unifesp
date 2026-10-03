import cv2 #importa biblioteca OpenCV

#Carregando imagem e segmentando canais
imagem = cv2.imread("./Imagens/baboon.jpg")
azul, verde, vermelho = cv2.split(imagem)

#Exibindo imagens dos canais separados
cv2.imshow("Imagem RGB", imagem)
cv2.imshow("Canal R", vermelho)
cv2.imshow("Canal G", verde)
cv2.imshow("Canal B", azul)

cv2.waitKey(0)
cv2.destroyAllWindows()

