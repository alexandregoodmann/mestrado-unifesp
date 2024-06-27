
import mylib
import cv2
import os

os.system('cls' if os.name == 'nt' else 'clear')

# ------------------------------------------------------------------------------------
# Teste para cortar imagem em pedacos
# ------------------------------------------------------------------------------------
def cortarImagemTest():
    imgGray = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/Screenshot from 2024-05-10 12-17-32.png')
    partes = mylib.cortarImagem(imgGray, 2, 3)

    if (partes.__len__() != 6):
        RuntimeError('cortarImagemTest - [ERROR]')
    else:
        print('cortarImagemTest - [OK]')

    for i in range(0, partes.__len__()):
        cv2.imwrite('/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/parte_' + str(i+1) +'.png', partes[i])
        cv2.imshow('Imagem Binaria', partes[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# ------------------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------------------
# cortarImagemTest()

img = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/imagem_original.png')
nova = cv2.imwrite('/home/alexandre/projetos/mestrado-unifesp/pi/artigo/imgs/imagem_reduzida.png', img[::2,::2])