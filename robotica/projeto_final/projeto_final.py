from turtle import clear
import numpy as np
import matplotlib.pyplot as plt

import sim 
import os
import logging
import time
import mylib

logging.basicConfig(level=logging.INFO, filename="/home/alexandre/projetos/mestrado-unifesp/robotica/atividade_2/pid.log", format="%(asctime)s - %(levelname)s - %(message)s")

# limpar console
os.system('cls' if os.name == 'nt' else 'clear')
# -------------------------------------------------------------------------------------------------------------------------------------
# Normalize angle to the range [-pi,pi)
def normalizeAngle(angle):
    return np.mod(angle+np.pi, 2*np.pi) - np.pi
# -------------------------------------------------------------------------------------------------------------------------------------
def getPosition():
    returnCode, ori = sim.simxGetObjectOrientation(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)  
    returnCode, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)
    return np.array([pos[0], pos[1], ori[2]])
# -------------------------------------------------------------------------------------------------------------------------------------

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim

if clientID!=-1:
    #----------------------
    # constantes programa
    #----------------------

    print ('Connected to remote API server')
    robotname = 'Pioneer_p3dx'
    returnCode, robotHandle = sim.simxGetObjectHandle(clientID, robotname, sim.simx_opmode_oneshot_wait)    
    returnCode, robotLeftMotorHandle  = sim.simxGetObjectHandle(clientID, robotname + '_leftMotor', sim.simx_opmode_oneshot_wait)
    returnCode, robotRightMotorHandle = sim.simxGetObjectHandle(clientID, robotname + '_rightMotor', sim.simx_opmode_oneshot_wait)
        
    # Goal configuration (x, y, theta)
    goal_1 = np.array([3.25, 3, np.deg2rad(0)])
    '''
    goal_1 = np.array([3.75, -3.75, np.deg2rad(90)])
    goal_1 = np.array([1, 1, np.deg2rad(180)])
    goal_2 = np.array([-3.25, -3.75, np.deg2rad(0)])
    goal_3 = np.array([-2.75, 3.25, np.deg2rad(0)])
    # Frame que representa o Goal
    returnCode, goalFrame = sim.simxGetObjectHandle(clientID, 'Goal', sim.simx_opmode_oneshot_wait)     
    returnCode = sim.simxSetObjectPosition(clientID, goalFrame, -1, [qgoal[0], qgoal[1], 0], sim.simx_opmode_oneshot_wait)
    returnCode = sim.simxSetObjectOrientation(clientID, goalFrame, -1, [0, 0, qgoal[2]], sim.simx_opmode_oneshot_wait)    
    '''
    
    # Específico do robô
    L = 0.331
    r = 0.09751
    maxv = 0.4
    maxw = np.deg2rad(45)
    
    distancia = np.inf
    while distancia > .05:
        
        position = getPosition()
        dx, dy, dth = goal_1 - position
        
        distancia = np.sqrt(dx**2 + dy**2)
        alpha = normalizeAngle(-position[2] + np.arctan2(dy,dx))
        beta = normalizeAngle(goal_1[2] - np.arctan2(dy,dx))
        
        kr = 4 / 20
        ka = 8 / 20
        kb = -1.5 / 20
        
        # Alvo na parte de trás
        if abs(alpha) > np.pi/2:
            kr = -kr       
            # Se não ajustar a direção muda
            alpha = normalizeAngle(alpha-np.pi)
            beta = normalizeAngle(beta-np.pi)
        
        v = kr*distancia
        w = ka*alpha + kb*beta
        
        # Limit v,w to +/- max
        v = max(min(v, maxv), -maxv)
        w = max(min(w, maxw), -maxw)        
        
        wr = ((2.0*v) + (w*L))/(2.0*r)
        wl = ((2.0*v) - (w*L))/(2.0*r)

        sim.simxSetJointTargetVelocity(clientID, robotRightMotorHandle, wr, sim.simx_opmode_oneshot_wait)
        sim.simxSetJointTargetVelocity(clientID, robotLeftMotorHandle, wl, sim.simx_opmode_oneshot_wait)

    print(position[:2], np.rad2deg(position[2]))    
    mylib.pararSimulacao(clientID)
    
else:
    print ('Failed connecting to remote API server')
    
print ('Program ended')