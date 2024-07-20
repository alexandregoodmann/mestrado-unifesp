import numpy as np
import cv2
from skimage.draw import line

imagem = np.zeros((1000, 1000))
imagem[::] = 255
cv2.imwrite('/home/alexandre/projetos/mestrado-unifesp/robotica/projeto_final/grid.png', imagem)
print('fim')