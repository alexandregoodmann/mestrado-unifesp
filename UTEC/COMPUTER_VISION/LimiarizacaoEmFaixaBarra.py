import cv2 as cv

valor_maximo = 255
val_max_H = 360 // 2
menor_H = 0
menor_S = 0
menor_V = 0
maior_H = val_max_H
maior_S = valor_maximo
maior_V = valor_maximo
nome_janela = 'Deteccao Objeto'
nome_menor_H = 'Menor H'
nome_menor_S = 'Menor S'
nome_menor_V = 'Menor V'
nome_maior_H = 'Maior H'
nome_maior_S = 'Maior S'
nome_maior_V = 'Maior V'


def ao_trocar_limiar_menor_H(val):
    global menor_H
    global maior_H
    menor_H = val
    menor_H = min(maior_H - 1, menor_H)
    cv.setTrackbarPos(nome_menor_H, nome_janela, menor_H)


def ao_troca_maior_H(val):
    global menor_H
    global maior_H
    maior_H = val
    maior_H = max(maior_H, menor_H + 1)
    cv.setTrackbarPos(nome_maior_H, nome_janela, maior_H)


def ao_trocar_menor_S(val):
    global menor_S
    global maior_S
    menor_S = val
    menor_S = min(maior_S - 1, menor_S)
    cv.setTrackbarPos(nome_menor_S, nome_janela, menor_S)


def ao_trocar_maior_S(val):
    global menor_S
    global maior_S
    maior_S = val
    maior_S = max(maior_S, menor_S + 1)
    cv.setTrackbarPos(nome_maior_S, nome_janela, maior_S)


def ao_trocar_menor_V(val):
    global menor_V
    global maior_V
    menor_V = val
    menor_V = min(maior_V - 1, menor_V)
    cv.setTrackbarPos(nome_menor_V, nome_janela, menor_V)


def ao_troca_maior_V(val):
    global menor_V
    global maior_V
    maior_V = val
    maior_V = max(maior_V, menor_V + 1)
    cv.setTrackbarPos(nome_maior_V, nome_janela, maior_V)


cv.namedWindow(nome_janela)
cv.createTrackbar(nome_menor_H, nome_janela, menor_H, val_max_H, ao_trocar_limiar_menor_H)
cv.createTrackbar(nome_maior_H, nome_janela, maior_H, val_max_H, ao_troca_maior_H)
cv.createTrackbar(nome_menor_S, nome_janela, menor_S, valor_maximo, ao_trocar_menor_S)
cv.createTrackbar(nome_maior_S, nome_janela, maior_S, valor_maximo, ao_trocar_maior_S)
cv.createTrackbar(nome_menor_V, nome_janela, menor_V, valor_maximo, ao_trocar_menor_V)
cv.createTrackbar(nome_maior_V, nome_janela, maior_V, valor_maximo, ao_troca_maior_V)

frame = cv.imread("c3.jpg");


frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

while True:
    frame_threshold = cv.inRange(frame_HSV, (menor_H, menor_S, menor_V), (maior_H, maior_S, maior_V))
    cv.imshow(nome_janela, frame_threshold)
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break