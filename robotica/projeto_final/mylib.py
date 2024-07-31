import sim 
import math
import numpy as np
import json
import time

def pararSimulacao(clientID):
    
    # Parando a simulação     
    stop = sim.simxStopSimulation(clientID,sim.simx_opmode_blocking)         
    
    # Finaliza conexao com CoppeliaSim:
    finish = sim.simxFinish(clientID)
    print('stop', stop, finish)

    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)

# ---------------------------------------------------------------------------------------
def getFuncaoReta(origem, destino):
    x = np.array([origem[0], destino[0]])
    y = np.array([origem[1], destino[1]])
    coefficients = np.polyfit(x, y, 1)
    a, b = coefficients
    print(f"Equação da linha ajustada: y = {a:.2f}x + {b:.2f}")
    return a, b

def isOnLine(x, y, a, b):
    fx = a*x + b
    inf = fx - 0.1
    sup = fx + 0.1
    if (y >= inf and y <= sup):
        return True
    return False
'''
origem = np.array([1, 2])
destino = np.array([3, 4])
a, b = getFuncaoReta(origem, destino)

print(isOnLine(1.5, 2.5))
'''
# ---------------------------------------------------------------------------------------
def prepararLidar(lidar_read):
    coordenadas = []
    if (lidar_read.__len__() == 2):
        angulos = lidar_read[0]
        distancias = lidar_read[1]
        for i in range(0, angulos.__len__()):
            xy = (angulos[i], distancias[i])
            coordenadas.append(xy)
    return coordenadas
# ---------------------------------------------------------------------------------------
def gravarArquivoLidar(position, lidar_coord, shotlidar):
    file_path = "/home/alexandre/projetos/mestrado-unifesp/robotica/projeto_final/lidar/teste2.txt"
    for c in lidar_coord:
        linha = str(position[0]) + ',' + str(position[1]) + ',' + str(position[2]) + ',' + str(c[0]) + ',' + str(c[1]) + ',' + str(shotlidar) + '\n' 
        with open(file_path, 'a') as arquivo:
            #json.dump(data, arquivo, ensure_ascii=False, indent=4)
            arquivo.write(linha)