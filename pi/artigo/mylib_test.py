import cv2
import os
import mylib

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')

dir = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/'
filename = 'sperm_3.png'

# ------------------------------------------------------------------------------------
# Cria uma imagem cinza no tamanha 9x9
# ------------------------------------------------------------------------------------
def abrirImagemTeste():
    #imgGray = cv2.imread(dir + filename, cv2.COLOR_BGR2GRAY)
    img = cv2.imread(dir + filename, cv2.COLOR_BGR2GRAY)
    img[:,:] = (255,255,255)
    print('Shape Imagem Test', img.shape)
    cv2.imshow('Imagem Test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img

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
#imgGray[:,:] = 180
#mylib.setConvolucao(imgGray, 4, 4, 1)
pontos = mylib.procuraCelula(imgGray, 15, 195, 20)
print('pontos', pontos)
#conv = mylib.getConvolucao(imgGray, 4, 4, 1)
#print('convolucao\n', conv)
cv2.imwrite(dir+filename, imgGray)
cv2.imshow('Imagem Test', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

