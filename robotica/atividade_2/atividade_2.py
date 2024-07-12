####################################################################################
#                                                                                  #
#                 LEMBRE-SE QUE A SIMULAÇÃO DEVE ESTAR EM EXECUÇÃO!                #
#                                                                                  #
####################################################################################

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
def printPositionAndOrientation():
    returnCode, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)        
    returnCode, ori = sim.simxGetObjectOrientation(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)
    print('Position: ', pos, 'Orientation: ', int(math.degrees(ori[0])), int(math.degrees(ori[1])), int(math.degrees(ori[2])))
# ---------------------------------------------------------------------------------------

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim

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
    gain = np.array([[0.2, 0, 0], [0, 0.2, 0], [0, 0, 0.2]])
    
    printPositionAndOrientation()
    inicio = time.time()
    errors = []
    for goal in goals:
        # Lembrar de habilitar o 'Real-time mode'
        while True:
                    
            returnCode, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)        
            returnCode, ori = sim.simxGetObjectOrientation(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)
            # print('pos', pos)
            # print('ori', ori)
            q = np.array([pos[0], pos[1], ori[2]])
            
            error = goal - q
            #print('error', error)
            
            # Margem aceitável de distância
            if (np.linalg.norm(error[:2]) < 0.05):
                break

            # Controllere
            qdot = gain @ error
            
            # Cinemática Inversa
            # w1, w2, w3
            Minv = np.linalg.inv(Rz(q[2]) @ Mdir)
            u = Minv @ qdot
            
            # Enviando velocidades
            sim.simxSetJointTargetVelocity(clientID, wheel1, u[0], sim.simx_opmode_streaming)
            sim.simxSetJointTargetVelocity(clientID, wheel2, u[1], sim.simx_opmode_streaming)
            sim.simxSetJointTargetVelocity(clientID, wheel3, u[2], sim.simx_opmode_streaming)          

        printPositionAndOrientation()   
    final = time.time()
    print('tempo', final - inicio) 
    pararSimulacao()

else:
    print ('Failed connecting to remote API server')
    
print ('Program ended')