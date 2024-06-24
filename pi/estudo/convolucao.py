import numpy as np
import math
import cv2
from matplotlib import pyplot as plt

kernel = np.array([[0,1,0],[1,0,1],[0,1,0]])
image = np.array([[161,137,244],[154,169,200],[112,126,143]])

print('kernel', kernel)
print('image', math.ceil(np.average(image)))

img = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio1/Lenna.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def blurImage(img):
    blur = np.zeros(img.shape)
    w, h = img.shape
    for i in range(1, w-1):
        for j in range(1, h-1):
            convolucao = img[i-1:i+1, j-1:j+1]
            media = np.average(convolucao)
            blur[i, j] = media
    return blur

def sharpOrEdge(img, option=5):
    sharp = np.zeros(img.shape)
    w, h = img.shape
    for i in range(1, w-1):
        for j in range(1, h-1):
            #convolucao = img[i-1:i+1, j-1:j+1]
            center = img[i,j] * option
            soma = center - img[i-1,j] - img[i+1,j] - img[i,j-1] - img[i,j+1]
            sharp[i,j] = soma
    return sharp

imgBlur = blurImage(imgGray)
imgSharp = sharpOrEdge(imgGray, 5)
imgEdge = sharpOrEdge(imgGray, 4)

plt.subplot(141),plt.imshow(imgGray, cmap='gray'),plt.title('ORIGINAL')
plt.subplot(142),plt.imshow(imgBlur, cmap='gray'),plt.title('BLUR')
plt.subplot(143),plt.imshow(imgSharp, cmap='gray'),plt.title('SHARP')
plt.subplot(144),plt.imshow(imgEdge, cmap='gray'),plt.title('EDGE')
plt.show()