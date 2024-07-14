from turtle import clear
import numpy as np
import matplotlib.pyplot as plt

import math
import sim 
import os
import logging
import time

# limpar console
os.system('cls' if os.name == 'nt' else 'clear')

# ---------------------------------------------------------------------------------------
def Rz(theta):
    return np.array([[ np.cos(theta), -np.sin(theta), 0 ],
                      [ np.sin(theta), np.cos(theta) , 0 ],
                      [ 0            , 0             , 1 ]])
# ---------------------------------------------------------------------------------------
def pararSimulacao():
    
    # Parando a simulação     
    stop = sim.simxStopSimulation(clientID,sim.simx_opmode_blocking)         
    
    # Finaliza conexao com CoppeliaSim:
    finish = sim.simxFinish(clientID)
    print('stop', stop, finish)

    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
# ---------------------------------------------------------------------------------------
def pararRobo():
    sim.simxSetJointTargetVelocity(clientID, wheel1, 0, sim.simx_opmode_oneshot_wait)
    sim.simxSetJointTargetVelocity(clientID, wheel2, 0, sim.simx_opmode_oneshot_wait)
    sim.simxSetJointTargetVelocity(clientID, wheel3, 0, sim.simx_opmode_oneshot_wait)
# ---------------------------------------------------------------------------------------
def setFrameGoal(qgoal):
    # Goal configuration (x, y, theta)    
    # qgoal = np.array([2, 2, np.deg2rad(90)])
    # Frame que representa o Goal
    returnCode, goalFrame = sim.simxGetObjectHandle(clientID, 'Goal', sim.simx_opmode_oneshot_wait)     
    returnCode = sim.simxSetObjectPosition(clientID, goalFrame, -1, [qgoal[0], qgoal[1], 0], sim.simx_opmode_oneshot_wait)
    returnCode = sim.simxSetObjectOrientation(clientID, goalFrame, -1, [0, 0, qgoal[2]], sim.simx_opmode_oneshot_wait)

# ---------------------------------------------------------------------------------------
# CONTROLADORES
# ---------------------------------------------------------------------------------------
Kp = np.array([[0.2, 0, 0], [0, 0.2, 0], [0, 0, 0.2]])
Kd = np.array([[0.02, 0, 0], [0, 0.02, 0], [0, 0, 0.02]])
Ki = np.array([[0.002, 0, 0], [0, 0.002, 0], [0, 0, 0.002]])
dt = 0.05

# CONTROLADOR P - u(t) = Kp * e(t)
def controlador_P(erro):
    controle = Kp @ erro
    return controle

# CONTROLADOR D - u(t) = Kd * de(t)/dt
def controlador_D(erro, erro_anterior):
    derivada_erro = (erro - erro_anterior) / dt
    controle = Kd @ derivada_erro
    return controle

def controlador_I(erro_acumulado):
    return Ki @ erro_acumulado
# ---------------------------------------------------------------------------------------

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to CoppeliaSim

# Goal
goals = []
qgoal_1 = np.array([3, 0, np.deg2rad(90)])
qgoal_2 = np.array([3, 3, np.deg2rad(180)])
qgoal_3 = np.array([0, 3, np.deg2rad(180)])
qgoal_4 = np.array([0, 0, np.deg2rad(0)])
goals.append(qgoal_1)
goals.append(qgoal_2)
goals.append(qgoal_3)
goals.append(qgoal_4)

if clientID!=-1:

    print ('Connected to remote API server')

    robotname = 'robotino'
    returnCode, robotHandle = sim.simxGetObjectHandle(clientID, robotname, sim.simx_opmode_oneshot_wait)     
                 
    returnCode, wheel1 = sim.simxGetObjectHandle(clientID, 'wheel0_joint', sim.simx_opmode_oneshot_wait)
    returnCode, wheel2 = sim.simxGetObjectHandle(clientID, 'wheel1_joint', sim.simx_opmode_oneshot_wait)
    returnCode, wheel3 = sim.simxGetObjectHandle(clientID, 'wheel2_joint', sim.simx_opmode_oneshot_wait)
               
    # Robotino
    L = 0.135   # Metros
    r = 0.040   # Metros
               
    # Cinemática Direta
    Mdir = np.array([[-r/np.sqrt(3), 0, r/np.sqrt(3)], [r/3, (-2*r)/3, r/3], [r/(3*L), r/(3*L), r/(3*L)]])
    
    tempo_inicial = time.time()
    for goal in goals:
        erro_anterior = np.array([0, 0, 0])
        erro_acumulado = np.array([0, 0, 0])
        # Lembrar de habilitar o 'Real-time mode'
        while True:
                    
            returnCode, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)        
            returnCode, ori = sim.simxGetObjectOrientation(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)
            position = np.array([pos[0], pos[1], ori[2]])

            # Controlador
            erro = goal - position
            erro_acumulado = erro_acumulado + (erro * dt)
            p = controlador_P(erro)
            d = controlador_D(erro, erro_anterior)
            i = controlador_I(erro_acumulado)
            controle = p + d + i
            erro_anterior = erro

            # Margem aceitável de distância
            if (np.linalg.norm(erro[:2]) < 0.05):
                break
            
            # Cinemática Inversa
            # w1, w2, w3
            Minv = np.linalg.inv(Rz(position[2]) @ Mdir)
            u = Minv @ controle
            
            # Enviando velocidades
            sim.simxSetJointTargetVelocity(clientID, wheel1, u[0], sim.simx_opmode_streaming)
            sim.simxSetJointTargetVelocity(clientID, wheel2, u[1], sim.simx_opmode_streaming)
            sim.simxSetJointTargetVelocity(clientID, wheel3, u[2], sim.simx_opmode_streaming)          

    tempo_final = time.time()

    print('dt', dt)
    print('Tempo percurso:', tempo_final - tempo_inicial) 
    pararSimulacao()

else:
    print ('Failed connecting to remote API server')
    
print ('Program ended')