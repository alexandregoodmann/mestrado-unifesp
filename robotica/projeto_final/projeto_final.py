import numpy as np
import sim
import mylib
import os
from skimage.draw import line
import cv2

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
laser_range_data = "hokuyo_range_data"
laser_angle_data = "hokuyo_angle_data"

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
    obstacle_in_front = (detected_front and np.linalg.norm(point_front) < .35)
    obstacle_in_right = (detected_right and np.linalg.norm(point_right) < .35)
    obstacle_in_left = (detected_left and np.linalg.norm(point_left) < .35)
    return obstacle_in_front, obstacle_in_right, obstacle_in_left
# ---------------------------------------------------------------------------------------
def setFrameGoal(qgoal):
    # Goal configuration (x, y, theta)    
    # qgoal = np.array([2, 2, np.deg2rad(90)])
    # Frame que representa o Goal
    returnCode, goalFrame = sim.simxGetObjectHandle(clientID, 'Goal', sim.simx_opmode_oneshot_wait)     
    returnCode = sim.simxSetObjectPosition(clientID, goalFrame, -1, [qgoal[0], qgoal[1], 0], sim.simx_opmode_oneshot_wait)
    returnCode = sim.simxSetObjectOrientation(clientID, goalFrame, -1, [0, 0, qgoal[2]], sim.simx_opmode_oneshot_wait)
# ---------------------------------------------------------------------------------------
def writeLine(x0, y0, xn, yn, imagem):
    vetor_x, vetor_y = line(int(x0), int(y0), int(xn), int(yn))
    for i in range(0, vetor_x.__len__()):
        x = vetor_x[i]
        y = vetor_y[i]
        imagem[x,y] = 0
# ---------------------------------------------------------------------------------------
def criarImagem(grid):
    print('INFO - criando imagem')
    imagem = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/robotica/projeto_final/grid.png')
    imagem[::] = 255
    for item in grid:
        x0 = int(item[0]*100) + 499
        y0 = int(item[1]*100) + 499
        xn = int(item[2]*100) + 499
        yn = int(item[3]*100) + 499
        if (x0 > 999): x0 = 999
        if (y0 > 999): y0 = 999
        if (xn > 999): xn = 999
        if (yn > 999): yn = 999
        writeLine(x0, y0, xn, yn, imagem)
    cv2.imwrite('/home/alexandre/projetos/mestrado-unifesp/robotica/projeto_final/grid.png', imagem)
    print('INFO - imagem criada')
# ---------------------------------------------------------------------------------------
def getLidar(clientID, laser_range_data, laser_angle_data):
    lidar = readSensorData(clientID, laser_range_data, laser_angle_data)
    angulo, medida = lidar[1], lidar[0]
    meio = int(medida.__len__()/2)
    return angulo[meio], medida[meio]
# ---------------------------------------------------------------------------------------
def getCoordenadaObstaculo(x, y, th, D):
    X = np.cos(th) * D + x
    Y = np.sin(th) * D + y
    return X, Y
# ---------------------------------------------------------------------------------------
def readSensorData(clientId, rangeid="hokuyo_range_data", angleid="hokuyo_angle_data"):
    range, angle = [0], [0]
    returnCodeRanges, string_range = sim.simxGetStringSignal(clientId, rangeid, sim.simx_opmode_streaming)
    returnCodeAngles, string_angle = sim.simxGetStringSignal(clientId, angleid, sim.simx_opmode_blocking)
    if (returnCodeRanges == 0 and returnCodeAngles == 0):
        range = sim.simxUnpackFloats(string_range)
        angle = sim.simxUnpackFloats(string_angle)
    return np.array([range, np.rad2deg(angle)])
# ----------------------------------------------------------------------------------------------
# BLOCO IMPLEMENTAÇÃO BUT ALGORITHM
# ----------------------------------------------------------------------------------------------
following = False
v = .4
w = 0
maxv = 0.4
maxw = np.deg2rad(45)

goals = []
goal_1 = np.array([3.75, -3.75, np.deg2rad(0)])
goal_2 = np.array([-3.25, -3.75, np.deg2rad(0)])
goal_3 = np.array([-2.75, 3.25, np.deg2rad(0)])
goal_4 = np.array([3.25, 3, np.deg2rad(0)])
goals = np.array([goal_2, goal_3, goal_4, goal_1])
grid = []

for goal in goals:
    setFrameGoal(goal)
    rho = np.inf
    while rho > 0.5:

        # Busca pelo destino
        position = getPosition()
        dx, dy, dth = goal - position

        # ------------------------------------------------------------------------
        # LIDAR
        # ------------------------------------------------------------------------
        # lidar_data.append(readSensorData(clientID, laser_range_data, laser_angle_data))
        angulo_lidar, distancia_lidar = getLidar(clientID, laser_range_data, laser_angle_data)
        X, Y = getCoordenadaObstaculo(position[0], position[1], position[2], distancia_lidar)
        grid.append([position[0], position[1],  X, Y])
        # ------------------------------------------------------------------------

        rho = np.sqrt(dx**2 + dy**2)
        alpha = normalizeAngle(-position[2] + np.arctan2(dy,dx))
        beta = normalizeAngle(goal[2] - np.arctan2(dy,dx))

        kr = 4 / 20
        ka = 8 / 20
        kb = -1.5 / 20

        v = kr*rho
        w = ka*alpha + kb*beta
        
        # Limit v,w to +/- max
        v = max(min(v, maxv), -maxv)
        w = max(min(w, maxw), -maxw)  

        # ------------------------------------------------------------------------
        # BUG ALGORITHM
        # ------------------------------------------------------------------------
        obstacle_in_front, obstacle_in_right, obstacle_in_left = getObstacle()
        following = obstacle_in_front
        # Controle
        if obstacle_in_front:
            v = 0
            w = np.deg2rad(30)
            following = True
        else: 
            if (obstacle_in_right or obstacle_in_right):
                w = np.deg2rad(10)
            elif following:
                v = .1
                w = np.deg2rad(-30)
        # ------------------------------------------------------------------------

        wr = ((2.0*v) + (w*L))/(2.0*r)
        wl = ((2.0*v) - (w*L))/(2.0*r)

        sim.simxSetJointTargetVelocity(clientID, r_wheel, wr, sim.simx_opmode_oneshot_wait)
        sim.simxSetJointTargetVelocity(clientID, l_wheel, wl, sim.simx_opmode_oneshot_wait)
        # --- Fim de um trecho (goal)
    print('trecho: ', getPosition())
    #print(grid)
    criarImagem(grid)

# --- Fim dos 4 Blocos de execucao------------------------------------------------------------------------

mylib.pararSimulacao(clientID)
exit()