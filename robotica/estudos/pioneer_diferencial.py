import sim 
import numpy as np
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to CoppeliaSim

if clientID!=-1:
    print ('Connected to remote API server')

    robotname = 'Pioneer_p3dx'
    returnCode, robotHandle = sim.simxGetObjectHandle(clientID, robotname, sim.simx_opmode_oneshot_wait)     
        
    returnCode, l_wheel = sim.simxGetObjectHandle(clientID, robotname + '_leftMotor', sim.simx_opmode_oneshot_wait)
    returnCode, r_wheel = sim.simxGetObjectHandle(clientID, robotname + '_rightMotor', sim.simx_opmode_oneshot_wait)    
           
    # Específico do robô
    # https://www.generationrobots.com/media/Pioneer3DX-P3DX-RevA.pdf
    # L = 0.381   # Metros
    # r = 0.0975  # Metros
    
    L = 0.331
    r = 0.09751
    
    # Velocidade desejada (linear, angular)
    v = .3
    w = np.deg2rad(0)

    # Cinemática Inversa
    wr = ((2.0*v) + (w*L))/(2.0*r)
    wl = ((2.0*v) - (w*L))/(2.0*r)    
    u = np.array([wr, wl])

    # Enviando velocidades
    sim.simxSetJointTargetVelocity(clientID, l_wheel, wl, sim.simx_opmode_oneshot_wait)
    sim.simxSetJointTargetVelocity(clientID, r_wheel, wr, sim.simx_opmode_oneshot_wait)
    
    q = np.array([0, 0, 0])
    
    t = 0
    # Lembrar de habilitar o 'Real-time mode'
    startTime=time.time()
    lastTime = startTime
    returnCode, p1 = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)    
    print('posicao inicial', p1)

    while t < 10:
        
        now = time.time()
        dt = now - lastTime

        # Cinemática Direta
        Mdir = np.array([[r*np.cos(q[2])/2, r*np.cos(q[2])/2], [r*np.sin(q[2])/2, r*np.sin(q[2])/2], [r/L, -r/L]])
        q = q + (Mdir @ u)*dt
        
        t = t + dt        
        lastTime = now
    
    #print('==> ', t, q[:2], np.rad2deg(q[2]))
    print('==> ', q)

    returnCode, p2 = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)    
    print('posicao final', p2) 
    print('diff posicao', np.subtract(p2, p1))
    
    sim.simxSetJointTargetVelocity(clientID, r_wheel, 0, sim.simx_opmode_oneshot_wait)
    sim.simxSetJointTargetVelocity(clientID, l_wheel, 0, sim.simx_opmode_oneshot_wait)
        
    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
    
else:
    print ('Failed connecting to remote API server')
    
print ('Program ended')