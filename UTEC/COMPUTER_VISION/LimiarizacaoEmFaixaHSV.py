import cv2 as cv
# Cria as janelas de visualizacao
nome_janela = "Resultado Limiarizacao Em Faixa"
nome_janela_img_orig = "Imagem Original"
cv.namedWindow(nome_janela)
cv.namedWindow(nome_janela_img_orig)
# Define os parametros de limiarização
menor_H = 104; maior_H = 112
menor_S = 66; maior_S = 229
menor_V = 113; maior_V = 215
# Carrega a imagem
imagem = cv.imread("c3.jpg")
# Converte a imagem do espaço BGR pro HSV
imagem_HSV = cv.cvtColor(imagem, cv.COLOR_BGR2HSV)
cv.imshow(nome_janela_img_orig, imagem) # Mostra a imagem
# Aplica a limiarização
imagem_limitada = cv.inRange(imagem_HSV, (menor_H, menor_S, menor_V), (maior_H, maior_S, maior_V))
cv.imshow(nome_janela, imagem_limitada) # Mostra o resultado
cv.waitKey(0)