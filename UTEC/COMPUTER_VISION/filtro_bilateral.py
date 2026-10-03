import cv2
from matplotlib import pyplot as plt

#Lê imagem colorida
imgOriginal =  cv2.imread("lena_RuidoGaussiano.jpg")

#Aplica filtro bilateral com máscara de ordem 9 e tanto sigma color quanto sigma space 100
imgTratada = cv2.bilateralFilter(imgOriginal, 9, 100, 100)

#define titulos e ordem das imagens para mostrar na tela
titles = ['Imagem Original','Filtro bilateral']
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