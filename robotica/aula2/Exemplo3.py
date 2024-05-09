from turtle import clear
import numpy as np
import matplotlib.pyplot as plt

import math
import sim 
import os
import logging

logging.basicConfig(level=logging.INFO, filename="programa.log", format="%(asctime)s - %(levelname)s - %(message)s")
os.system('cls' if os.name == 'nt' else 'clear')

def andar(eixo, distancia):
    
    # calcula o ponto final para o eixo informado
    r, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait) 
    origem = pos[eixo]
    destino = pos[eixo] + distancia 

    #faz o carro andar 
    sim.simxSetJointTargetVelocity(clientID, l_wheel, 3, sim.simx_opmode_streaming + 5)
    sim.simxSetJointTargetVelocity(clientID, r_wheel, 3, sim.simx_opmode_streaming + 5)

    posicao = origem
    if (posicao < destino):
        while (posicao < destino):
            r, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait) 
            print('vai', pos)
            posicao = pos[eixo]
    else:
        while (posicao > destino):
            r, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)  
            print('volta', pos)
            posicao = pos[eixo]

    pararRobo()

def curva(destino):
    sim.simxSetJointTargetVelocity(clientID, l_wheel, 1, sim.simx_opmode_streaming + 5)
    sim.simxSetJointTargetVelocity(clientID, r_wheel, -1, sim.simx_opmode_streaming + 5) 
    
    r, orientation = sim.simxGetObjectOrientation(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)
    atual = math.degrees(orientation[2])

    while (atual > destino):
        r, orientation = sim.simxGetObjectOrientation(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)
        print(math.degrees(orientation[0]), math.degrees(orientation[1]), math.degrees(orientation[2]))
        atual = math.degrees(orientation[2])

    pararRobo()

def printPositionAndOrientation():
    returnCode, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)  
    a, orientation = sim.simxGetObjectOrientation(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)
    print('Position: ', pos, 'Orientation: ', int(math.degrees(orientation[0])), int(math.degrees(orientation[1])), int(math.degrees(orientation[2])))

def pararRobo():
    sim.simxSetJointTargetVelocity(clientID, l_wheel, 0, sim.simx_opmode_oneshot_wait)  
    sim.simxSetJointTargetVelocity(clientID, r_wheel, 0, sim.simx_opmode_oneshot_wait)

def pararSimulacao():

    # Parando a simulação     
    sim.simxStopSimulation(clientID,sim.simx_opmode_blocking)         
        
    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)

sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to CoppeliaSim

if clientID!=-1:
    print ('Connected to remote API server')
    
    # Iniciando a simulação
    # Deve usar a porta do 'continuous remote API server services' (remoteApiConnections.txt)
    # e = sim.simxStartSimulation(clientID,sim.simx_opmode_blocking)

    # Handle para o ROBÔ    
    robotname = 'Pioneer_p3dx'
    returnCode, robotHandle = sim.simxGetObjectHandle(clientID, robotname, sim.simx_opmode_oneshot_wait)     
    
    # Handle para as juntas das RODAS
    returnCode, l_wheel = sim.simxGetObjectHandle(clientID, robotname + '_leftMotor', sim.simx_opmode_oneshot_wait)
    returnCode, r_wheel = sim.simxGetObjectHandle(clientID, robotname + '_rightMotor', sim.simx_opmode_oneshot_wait)    
    
    returnCode, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)   
    
    # Dados do Pioneer
    larguraRobo = 0.381   # Metros
    raioRoda = 0.0975  # Metros
    v_TangencialRoda = 0.3
    v_AngularRoda = np.deg2rad(0)  
    vAngular_esquerda = 3 #v_TangencialRoda/raioRoda - (v_AngularRoda*larguraRobo)/(2*raioRoda)
    vAngular_direita = 3 #v_TangencialRoda/raioRoda + (v_AngularRoda*larguraRobo)/(2*raioRoda)
    t = 0

    # Faz andar pra frente (vAngular, distancia, eixo)
    # trecho 1
    print('--->>> Inicio da Simulacao <<<---')
    printPositionAndOrientation()
    andar(1, 1)
    curva(0)

    # trecho 2
    printPositionAndOrientation()
    andar(0, 1)
    curva(-90)

    # trecho 3
    printPositionAndOrientation()
    andar(1, -1)
    curva(-179)

    # trecho 4
    printPositionAndOrientation()
    andar(0, -1)
    printPositionAndOrientation()
    print('--->>> Fim <<<---')
    # todo andar pra zero

    pararSimulacao()
    #exit()