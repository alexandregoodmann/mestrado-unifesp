import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from skimage.draw import line
os.system('cls' if os.name == 'nt' else 'clear')
# --------------------------------------------------------------------------
def Rz(theta):
    return np.array([[  np.cos(theta), -np.sin(theta), 0 ],
                      [ np.sin(theta),  np.cos(theta), 0 ],
                      [ 0            ,  0            , 1 ]])
# --------------------------------------------------------------------------
def calcularB(B, Borig, th):
    Rab = Rz(np.deg2rad(th))
    Tab = np.column_stack((Rab, Borig))
    aux = np.array([0, 0, 0, 1])
    Tab = np.row_stack((Tab, aux))
    A = Tab @ B
    return A
# --------------------------------------------------------------------------
def getLidarCoords(angle, range):
    angle = abs(float(angle) - 90)
    if (angle > 180):
        angle = 180
    elif(angle < 0):
        angle = 0
    x = np.cos(np.deg2rad(angle)) * float(range)
    y = np.sin(np.deg2rad(angle)) * float(range)
    return x, y
# --------------------------------------------------------------------------
def writeLine(x0, y0, xn, yn):
    vetor_x, vetor_y = line(int(x0), int(y0), int(xn), int(yn))
    for i in range(0, vetor_x.__len__()):
        x = vetor_x[i]
        y = vetor_y[i]
        imagem[x,y] = 0
# --------------------------------------------------------------------------

#           x-robot-position   y-robot-position    z-rotation(deg)   laser-angle        laser-distance
# linha = '-2.4836183190345764,4.338506102561951,-99.22280694074638,-90.00000250447816,4.999499797821045'

print('[INFO] - Inicio da Execucao')

imagem = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/robotica/outros/grid.png')
imagem[::] = 255

file_path = "/home/alexandre/projetos/mestrado-unifesp/robotica/projeto_final/exemplo.txt"
with open(file_path, 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        # Lê a linha do arquivo e Encontra XY do laser
        vet = linha.split(',')
        X_robo, Y_robo = float(vet[0]), float(vet[1])
        Xb, Yb = getLidarCoords(vet[3], vet[4])
        B = np.array([Xb, Yb, 0, 1])
        Borig = np.array([X_robo, Y_robo, 0])
        A = calcularB(B, Borig, 0)
        Ax, Ay = A[0], A[1]

        #Desenhar a linha na imagem. Origem é a posição do robo e destino é Ax, Ay
        x0 = int(X_robo*100) + 499
        y0 = int(Y_robo*100) + 499
        xn = int(Ax*100) + 499
        yn = int(Ay*100) + 499
        if (x0 > 999): x0 = 999
        if (y0 > 999): y0 = 999
        if (xn > 999): xn = 999
        if (yn > 999): yn = 999
        writeLine(x0, y0, xn, yn)

cv2.imwrite('/home/alexandre/projetos/mestrado-unifesp/robotica/outros/grid.png', imagem)
print('INFO - Fim')