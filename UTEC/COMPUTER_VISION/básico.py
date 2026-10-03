import cv2
import numpy as np
import imutils

#Lê imagem
imagem =  cv2.imread("./Imagens/baboon.jpg", cv2.IMREAD_COLOR)

#Cria uma janela e informa mostra a imagem
cv2.namedWindow('Nome da Janela', cv2.WINDOW_NORMAL)
cv2.imshow('Nome da Janela', imagem)

#Verifica quantidade de linhas, colunas e chanais
forma = imagem.shape
if(len(forma) == 3):
    print("Imagem colorida")
    print("Linhas: ", forma[0], "\nColunas: ", forma[1], "\nCanais: ",forma[2])
else:
    print("Imagem em escala de cinza")
    print("Linhas: ", forma[0], "\nColunas: ", forma[1])

#Verifica quantidade de píxeis
print("Quantidade de pixeis: ", imagem.size)

altura = imagem.shape[0]   # linhas
largura = imagem.shape[1]  # colunas
pixels = altura * largura
megapixels = pixels / 1_000_000

print("Megapixels:", megapixels, "MP")

#Salva imagem
cv2.imwrite('copia_baboon.jpg', imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()



