####################################################################################
#                                                                                  #
#                 Exemplo por Prof. Douglas Macharet - UFMG                        #
#                                                                                  #
####################################################################################
from turtle import clear
import numpy as np
import matplotlib.pyplot as plt

import math
import sim 
import time
import os
import logging

logging.basicConfig(level=logging.INFO, filename="programa.log", format="%(asctime)s - %(levelname)s - %(message)s")
os.system('cls' if os.name == 'nt' else 'clear')

def andarFrente(eixo):
    sim.simxSetJointTargetVelocity(clientID, l_wheel, 3, sim.simx_opmode_streaming + 5)
    sim.simxSetJointTargetVelocity(clientID, r_wheel, 3, sim.simx_opmode_streaming + 5)  

    posicao = 0
    while (posicao <= 1):
        returnCode, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)  
        posicao = pos[eixo]

    pararRobo()

def andarVolta(eixo):
    sim.simxSetJointTargetVelocity(clientID, l_wheel, 3, sim.simx_opmode_streaming + 5)
    sim.simxSetJointTargetVelocity(clientID, r_wheel, 3, sim.simx_opmode_streaming + 5)  

    posicao = 1
    while (posicao >= 0):
        returnCode, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)  
        posicao = pos[eixo]

    pararRobo()

def curvaDireita():
    sim.simxSetJointTargetVelocity(clientID, l_wheel, 1, sim.simx_opmode_streaming + 5)
    sim.simxSetJointTargetVelocity(clientID, r_wheel, -1, sim.simx_opmode_streaming + 5) 
    
    graus = 90
    while (graus > 0):
        a, orientation = sim.simxGetObjectOrientation(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)
        graus = math.degrees(orientation[2])
    pararRobo()

def curvaDireita2():
    sim.simxSetJointTargetVelocity(clientID, l_wheel, 1, sim.simx_opmode_streaming + 5)
    sim.simxSetJointTargetVelocity(clientID, r_wheel, -1, sim.simx_opmode_streaming + 5) 
    
    graus = 0
    while (graus > -90):
        a, orientation = sim.simxGetObjectOrientation(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)
        graus = math.degrees(orientation[2])
    pararRobo()

def curvaDireita3():
    sim.simxSetJointTargetVelocity(clientID, l_wheel, 1, sim.simx_opmode_streaming + 5)
    sim.simxSetJointTargetVelocity(clientID, r_wheel, -1, sim.simx_opmode_streaming + 5) 
    
    graus = -90
    while (graus <= 0):
        a, orientation = sim.simxGetObjectOrientation(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)
        graus = math.degrees(orientation[2])
    pararRobo()

def printPositionAndOrientation():
    returnCode, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)  
    a, orientation = sim.simxGetObjectOrientation(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)
    print('Position: ', [int(pos[0]), int(pos[1])], 'Orientation: ', int(math.degrees(orientation[0])), int(math.degrees(orientation[1])), int(math.degrees(orientation[2])))

def pararRobo():
    sim.simxSetJointTargetVelocity(clientID, r_wheel, 0, sim.simx_opmode_oneshot_wait)
    sim.simxSetJointTargetVelocity(clientID, l_wheel, 0, sim.simx_opmode_oneshot_wait)  

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
    printPositionAndOrientation()
    andarFrente(1)
    curvaDireita()

    # trecho 2
    printPositionAndOrientation()
    andarFrente(0)
    curvaDireita2()

    # trecho 3
    printPositionAndOrientation()
    andarVolta(1)
    curvaDireita3()

    # trecho 4
    printPositionAndOrientation()
    andarVolta(0)
    printPositionAndOrientation()
    # todo andar pra zero

    pararSimulacao()
    exit()