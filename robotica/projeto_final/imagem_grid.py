import numpy as np
import cv2

imagem = np.zeros((100, 100))
imagem[::] = 255
print(imagem)
cv2.imwrite('/home/alexandre/projetos/mestrado-unifesp/robotica/projeto_final/grid.png', imagem)