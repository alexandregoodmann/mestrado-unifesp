import cv2
import os
import mylib

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')

dir = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/'
filename = 'quadrado_prova.png'

# ------------------------------------------------------------------------------------
# Manipular cor em quadro especifico
# img[coluna, linha] --> diferente de notação matricial.
# img[3:6, :] --> Esta notação é do tipo [a,b[, ou seja fechado no início e aberto no final.
# Isso significa que tem que adicionar um no final para pegar o último pixel desejado
# img[3:6, :] = (0,0,0)
# ------------------------------------------------------------------------------------
def bordaQuadradaTest():
    imgMarked = mylib.setBordaQuadrada(0, img, 3, 3, 3, (0,0,255))
    cv2.imshow('Imagem marked', imgMarked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(dir+filename, imgMarked)
    return imgMarked

# -------------------
# MAIN
# -------------------
'''
img = cv2.imread(dir + filename)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGray[:,:] = 255
imgGray[1:3,1:3] = 180
h, w = imgGray.shape
#mylib.setBordaQuadrada(1, imgGray, 0, 0, 3, 0)
media = mylib.getIntensidadeMedia(imgGray, 1, 3, 1, 3)

print('media', media)
cv2.imwrite(dir+filename, imgGray)
cv2.imshow('Imagem Test', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
img = cv2.imread(dir + filename)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGray[:,:] = 180
imgGray[3, 2:5] = 0
imgGray[2,3] = 0
imgGray[2,2] = 0
#cv2.imwrite(dir+filename, imgGray)
cv2.imshow('Imagem Test', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, imgBW = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)
#imgBW = mylib.contaObjetos(imgBW,1)
imgBW, pontos = mylib.setBlank(imgBW, [2,2])

