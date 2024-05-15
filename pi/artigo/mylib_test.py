import cv2
import os
import mylib

# Limpar console
os.system('cls' if os.name == 'nt' else 'clear')

dir = '/home/alexandre/projetos/mestrado-unifesp/pi/artigo/'
filename = 'quadrado_prova.png'

# ------------------------------------------------------------------------------------
# Cria uma imagem cinza no tamanha 9x9
# ------------------------------------------------------------------------------------
def abrirImagemTeste():
    #imgGray = cv2.imread(dir + filename, cv2.COLOR_BGR2GRAY)
    img = cv2.imread(dir + filename)
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
img = abrirImagemTeste()
imgMarked = bordaQuadradaTest()
min, max = mylib.getIntensidadeMinMax(imgMarked, 3, 6, 3, 6, 0)
print('min max', min, max)




