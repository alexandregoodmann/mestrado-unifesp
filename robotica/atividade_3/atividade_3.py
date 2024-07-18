import numpy as np
import sim
import time
import mylib
import os

# ---------------------------------------------------------------------------------------
# BLOCO DE CONFIGURAÇÃO
# ---------------------------------------------------------------------------------------
os.system('cls' if os.name == 'nt' else 'clear')
print('[INFO] - Conectando ao CoppeliaSim')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim

if (clientID == -1):
    raise Exception("[ERRO] - Não foi possível conectar ao CoppeliaSim")

print('[INFO] - Conectado ao CoppeliaSim')

# Handles para robo
robotname = 'Pioneer_p3dx'
returnCode, robotHandle = sim.simxGetObjectHandle(clientID, robotname, sim.simx_opmode_oneshot_wait)     
returnCode, l_wheel = sim.simxGetObjectHandle(clientID, robotname + '_leftMotor', sim.simx_opmode_oneshot_wait)
returnCode, r_wheel = sim.simxGetObjectHandle(clientID, robotname + '_rightMotor', sim.simx_opmode_oneshot_wait)    

# Handles para os sonares
returnCode, sonar_front = sim.simxGetObjectHandle(clientID, robotname + '_ultrasonicSensor5', sim.simx_opmode_oneshot_wait)
returnCode, sonar_right = sim.simxGetObjectHandle(clientID, robotname + '_ultrasonicSensor7', sim.simx_opmode_oneshot_wait)
returnCode, sonar_left = sim.simxGetObjectHandle(clientID, robotname + '_ultrasonicSensor3', sim.simx_opmode_oneshot_wait)

# Específico do robô   
L = 0.331
r = 0.09751
# -------------------------------------------------------------------------------------------------------------------------------------
# Pega Posicao
# -------------------------------------------------------------------------------------------------------------------------------------
def getPosition():
    returnCode, ori = sim.simxGetObjectOrientation(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)  
    returnCode, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)
    return np.array([pos[0], pos[1], ori[2]])

# -------------------------------------------------------------------------------------------------------------------------------------
# Normalize angle to the range [-pi,pi)
# -------------------------------------------------------------------------------------------------------------------------------------
def normalizeAngle(angle):
    return np.mod(angle+np.pi, 2*np.pi) - np.pi
# -------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
# IDENTIFICAR UM OBSTACULO
# ---------------------------------------------------------------------------------------
def getObstacle():
    # Fazendo leitura dos sensores
    returnCode, detected_front, point_front, *_ = sim.simxReadProximitySensor(clientID, sonar_front, sim.simx_opmode_oneshot_wait)
    returnCode, detected_right, point_right, *_ = sim.simxReadProximitySensor(clientID, sonar_right, sim.simx_opmode_oneshot_wait)
    returnCode, detected_left, point_left, *_ = sim.simxReadProximitySensor(clientID, sonar_left, sim.simx_opmode_oneshot_wait)
    obstacle_in_front = (detected_front and np.linalg.norm(point_front) < .5)
    obstacle_in_right = (detected_right and np.linalg.norm(point_right) < .5)
    obstacle_in_left = (detected_left and np.linalg.norm(point_left) < .5)
    return obstacle_in_front, obstacle_in_right, obstacle_in_left

# ----------------------------------------------------------------------------------------------
# BLOCO IMPLEMENTAÇÃO BUT ALGORITHM
# ----------------------------------------------------------------------------------------------
following = False
v = .4
w = 0
maxv = 0.4
maxw = np.deg2rad(45)
goal_1 = np.array([-2.75, 4.25, np.deg2rad(0)])
goal_2 = np.array([2.25, -4.25, np.deg2rad(0)])
goals = [goal_1, goal_2]

for goal in goals:
    distancia = np.inf
    while distancia > .05:
        # Busca pelo destino
        position = getPosition()
        dx, dy, dth = goal - position
        distancia = np.sqrt(dx**2 + dy**2)
        alpha = normalizeAngle(-position[2] + np.arctan2(dy,dx))
        beta = normalizeAngle(goal[2] - np.arctan2(dy,dx))
        kr = 4 / 20
        ka = 8 / 20
        kb = -1.5 / 20
        v = kr*distancia
        w = ka*alpha + kb*beta
        
        # Limit v,w to +/- max
        v = max(min(v, maxv), -maxv)
        w = max(min(w, maxw), -maxw)        

        # ----------------------------------------------------------------------
        # Identifica Obstaculos
        obstacle_in_front, obstacle_in_right, obstacle_in_left = getObstacle()
        following = obstacle_in_front

        # Desvia dos obstaculos
        if obstacle_in_front:
            v = 0
            w = np.deg2rad(30)
            following = True
        else: 
            if obstacle_in_right:
                w = np.deg2rad(10)
            elif following:
                v = .1
                w = np.deg2rad(-30)
        # ----------------------------------------------------------------------
        
        wr = ((2.0*v) + (w*L))/(2.0*r)
        wl = ((2.0*v) - (w*L))/(2.0*r)

        sim.simxSetJointTargetVelocity(clientID, r_wheel, wr, sim.simx_opmode_oneshot_wait)
        sim.simxSetJointTargetVelocity(clientID, l_wheel, wl, sim.simx_opmode_oneshot_wait)

# --- Fim Bloco execucao------------------------------------------------------------------------

mylib.pararSimulacao(clientID)
exit()