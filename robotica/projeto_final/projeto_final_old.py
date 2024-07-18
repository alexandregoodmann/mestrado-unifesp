from turtle import clear
import numpy as np
import matplotlib.pyplot as plt

import sim 
import os
import logging
import time
import mylib

logging.basicConfig(level=logging.INFO, filename="/home/alexandre/projetos/mestrado-unifesp/robotica/projeto_final/lidar.log", format="%(asctime)s - %(levelname)s - %(message)s")

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
def getObstacle():
    # Fazendo leitura dos sensores
    returnCode, detected_front, point_front, *_ = sim.simxReadProximitySensor(clientID, sonar_front, sim.simx_opmode_oneshot_wait)
    returnCode, detected_right, point_right, *_ = sim.simxReadProximitySensor(clientID, sonar_right, sim.simx_opmode_oneshot_wait)
    returnCode, detected_left, point_left, *_ = sim.simxReadProximitySensor(clientID, sonar_left, sim.simx_opmode_oneshot_wait)
    obstacle_in_front = (detected_front and np.linalg.norm(point_front) < .35)
    obstacle_in_right = (detected_right and np.linalg.norm(point_right) < .35)
    obstacle_in_left = (detected_left and np.linalg.norm(point_left) < .35)
    return obstacle_in_front, obstacle_in_right, obstacle_in_left
# ---------------------------------------------------------------------------------------
def readSensorData(clientId, rangeid="hokuyo_range_data", angleid="hokuyo_angle_data"):
    range, angle = [0], [0]
    returnCodeRanges, string_range = sim.simxGetStringSignal(clientId, rangeid, sim.simx_opmode_streaming)
    returnCodeAngles, string_angle = sim.simxGetStringSignal(clientId, angleid, sim.simx_opmode_blocking)
    if (returnCodeRanges == 0 and returnCodeAngles == 0):
        range = sim.simxUnpackFloats(string_range)
        angle = sim.simxUnpackFloats(string_angle)
    return np.array([range, np.rad2deg(angle)])
# ---------------------------------------------------------------------------------------
def getLidar(clientID, laser_range_data, laser_angle_data):
    lidar = readSensorData(clientID, laser_range_data, laser_angle_data)
    angulo, medida = lidar[1], lidar[0]
    meio = int(medida.__len__()/2)
    return angulo[meio], medida[meio], getPosition()
# ---------------------------------------------------------------------------------------
def getCoordenadaObstaculo(x, y, th, D):
    X = np.cos(th) * D + x
    Y = np.sin(th) * D + y
    return X, Y
# ---------------------------------------------------------------------------------------

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

    # Handles para os sonares
    returnCode, sonar_front = sim.simxGetObjectHandle(clientID, robotname + '_ultrasonicSensor5', sim.simx_opmode_oneshot_wait)
    returnCode, sonar_right = sim.simxGetObjectHandle(clientID, robotname + '_ultrasonicSensor7', sim.simx_opmode_oneshot_wait)
    returnCode, sonar_left = sim.simxGetObjectHandle(clientID, robotname + '_ultrasonicSensor3', sim.simx_opmode_oneshot_wait)

    laser_range_data = "hokuyo_range_data"
    laser_angle_data = "hokuyo_angle_data"

    # Goal configuration (x, y, theta)
    goal_1 = np.array([3, 3, np.deg2rad(90)])
    
    # Específico do robô
    L = 0.331
    r = 0.09751
    maxv = 0.4
    maxw = np.deg2rad(45)
    distancia = np.inf
    lidar_data = []
    while distancia > .05:

        returnCode, detected_front, point_front, *_ = sim.simxReadProximitySensor(clientID, sonar_front, sim.simx_opmode_oneshot_wait)
        returnCode, detected_right, point_right, *_ = sim.simxReadProximitySensor(clientID, sonar_right, sim.simx_opmode_oneshot_wait)
        returnCode, detected_left, point_left, *_ = sim.simxReadProximitySensor(clientID, sonar_left, sim.simx_opmode_oneshot_wait)

        # lidar_data.append(readSensorData(clientID, laser_range_data, laser_angle_data))
        angulo_lidar, distancia_lidar, pos = getLidar(clientID, laser_range_data, laser_angle_data)
        X, Y = getCoordenadaObstaculo(pos[0], pos[1], pos[2], distancia_lidar)

        if (pos[1] > 0):
            print(distancia_lidar, pos[:2], np.rad2deg(pos[2]), X, Y)

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

    mylib.pararSimulacao(clientID)
    '''
    for data in lidar_data:
        medida = data[0]
        angulo = data[1]
        meio = int(medida.__len__()/2)
        print('angulo medida', meio, angulo[meio], medida[meio], getPosition())
    '''

else:
    print ('Failed connecting to remote API server')
    
print ('Program ended')