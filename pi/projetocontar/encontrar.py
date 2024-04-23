import cv2 as cv
import numpy as np
import io
from matplotlib import pyplot as plt

img = cv.imread('/home/alexandre/Documents/PI/projetocontar/imagem.webp')
assert img is not None, "file could not be read, check with os.path.exists()"
cv.imshow('Source Image', img)
cv.waitKey(0)
cv.destroyAllWindows()

#redimensionamento da imagem, proporcao 4:3
new_width = 640
new_heigth = 480
new_size = (new_width,new_heigth)
resize = cv.resize(img,new_size)

# conversao da imagem de BGR para HSV
img_hsv = cv.cvtColor(resize, cv.COLOR_BGR2HSV)
cv.imshow('Imagem em HSV', img_hsv)
cv.waitKey(0)
cv.destroyAllWindows()

#criacao das mascaras
blue_mask = cv.inRange(img_hsv,(90,66,153),(130,255,255))
green_mask = cv.inRange(img_hsv,(57,50,140),(75,255,255))
yellow_mask = cv.inRange(img_hsv,(22,30,190),(30,255,255))
first_brow_mask= cv.inRange(img_hsv,(140,15,80),(180,91,215))
second_brow_mask= cv.inRange(img_hsv,(0,15,75),(9,91,170))
red_mask = cv.inRange(img_hsv,(150,40,130),(180,255,255))
orange_mask = cv.inRange(img_hsv,(3,70,100),(13,255,255))

#juncao de imagens
or_mask_examples = cv.bitwise_or(blue_mask,green_mask)
or_mask_brow = cv.bitwise_or(first_brow_mask,second_brow_mask)

cv.imshow('Imagem em HSV', second_brow_mask)
cv.waitKey(0)
cv.destroyAllWindows()