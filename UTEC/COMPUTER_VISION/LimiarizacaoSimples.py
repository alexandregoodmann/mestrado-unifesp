import cv2 as cv
from matplotlib import pyplot as plt
# Carrega uma imagem (escala de cinza)
img = cv.imread('gradiente.png',0)
# Aplica diversos tipos de limiarização (Threshold)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
# Mostra o resultado
titles = ['Imagem Original','Binária','Binário Invertido',\
          'Trubcado','Para Zero','Para Zero Invertido']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# Mostra as imagens
for i in range(6):
   plt.subplot(2,3,i+1)
   plt.imshow(images[i],"gray")
   plt.title(titles[i])
   plt.xticks([])
   plt.yticks([])
plt.show()

# Necessário instalar python3-tk para rodar esse script usando o comando
# sudo apt install python3-tk