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
    Rab = Rz(th)
    Tab = np.column_stack((Rab, Borig))
    aux = np.array([0, 0, 0, 1])
    Tab = np.row_stack((Tab, aux))
    A = Tab @ B
    return A
# --------------------------------------------------------------------------
def getLidarCoords(angle, range):
    s_angle = angle*(-1) + np.deg2rad(90)
    d_angle = int(np.rad2deg(s_angle))
    if (d_angle >= 0 and d_angle <= 180):
        x = np.cos(s_angle) * float(range)
        y = np.sin(s_angle) * float(range)
        return x, y
# --------------------------------------------------------------------------
def writeLine(x0, y0, xn, yn):
    vetor_x, vetor_y = line(int(x0), int(y0), int(xn), int(yn))
    for i in range(0, vetor_x.__len__()):
        x = vetor_x[i]
        y = vetor_y[i]
        if (x < 1000 and y < 1000):
            imagem[x,y] = 0
# --------------------------------------------------------------------------

#           x-robot-position   y-robot-position    z-rotation(deg)   laser-angle        laser-distance
# linha = '-2.4836183190345764,4.338506102561951,-99.22280694074638,-90.00000250447816,4.999499797821045'

print('[INFO] - Inicio da Execucao')

imagem = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/robotica/projeto_final/lidar/grid.png')
imagem[::] = 255

file_path = "/home/alexandre/projetos/mestrado-unifesp/robotica/projeto_final/lidar/teste2_2.txt"
with open(file_path, 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        # Lê a linha do arquivo e Encontra XY do laser
        # -0.03499177470803261,1.986708402633667,7.981695087896203,-90.00000250447816,4.952520847320557
        vet = linha.split(',')
        X_robo, Y_robo = float(vet[0]), float(vet[1])
        Xb, Yb = getLidarCoords(float(vet[3]), float(vet[4]))
        B = np.array([Xb, Yb, 0, 1])
        Borig = np.array([X_robo, Y_robo, 0])
        A = calcularB(B, Borig, float(np.deg2rad(-90)))
        Ax, Ay = A[0], A[1]

        #Desenhar a linha na imagem. Origem é a posição do robo e destino é Ax, Ay
        x0 = int(X_robo*100) + 499
        y0 = int(Y_robo*100) + 499
        xn = int(Ax*100) + 499
        yn = int(Ay*100) + 499
        writeLine(x0, y0, xn, yn)

cv2.imwrite('/home/alexandre/projetos/mestrado-unifesp/robotica/projeto_final/lidar/grid2.png', imagem)
print('INFO - Fim')