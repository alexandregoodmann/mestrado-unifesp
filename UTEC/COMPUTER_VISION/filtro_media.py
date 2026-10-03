import cv2
from matplotlib import pyplot as plt

#Lê imagem colorida
imgOriginal =  cv2.imread("moedas.jpg")

#Aplica filtro de média com máscara de tamanho 5x5
imgTratada = cv2.blur(imgOriginal, (5,5))

#define titulos e ordem das imagens para mostrar na tela
titles = ['Imagem Original','Filtro de Média']
images = [imgOriginal, imgTratada]

for i in range(2):
   plt.subplot(1,2,i+1) #escolhe posição no subplot
   plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)) #utiliza imshow imagem convertendo de BGR para RGB
   plt.title(titles[i]) #coloca título
   # retira a representação dos eixos x e y
   plt.xticks([])
   plt.yticks([])

#mostra na tela
plt.show()