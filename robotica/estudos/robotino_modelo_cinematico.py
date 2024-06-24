import sim 
import numpy as np
import time

def Rz(theta):
    return np.array([[ np.cos(theta), -np.sin(theta), 0 ],
                      [ np.sin(theta), np.cos(theta) , 0 ],
                      [ 0            , 0             , 1 ]])

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to CoppeliaSim

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
                       
    q = np.array([0, 0, 0])
    
    # Lembrar de habilitar o 'Real-time mode'
    t = 0
    lastTime = time.time()
    while t <= 15:
        
        now = time.time()
        dt = now - lastTime
        
        # Cinemática Direta
        u = [np.deg2rad(45), np.deg2rad(0), np.deg2rad(-45)]
        
        # Velocidade desejada (x, y, w)    
       # if t <= 5:
       #     qdot = np.array([.2, 0, np.deg2rad(10)])
       # elif t <= 10:    
       #     qdot = np.array([0, -.2, np.deg2rad(-10)])
       # else:
       #     qdot = np.array([-.2, 0, 0])
        
        #qdot = np.array([0, .3, 0])
        
        # Cinemática Inversa
        # w1, w2, w3
        #Minv = np.linalg.inv(Rz(q[2]) @ Mdir)
        #u = Minv @ qdot

        # Enviando velocidades
        sim.simxSetJointTargetVelocity(clientID, wheel1, u[0], sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(clientID, wheel2, u[1], sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(clientID, wheel3, u[2], sim.simx_opmode_streaming)      
        
        q = q + (Rz(q[2]) @ Mdir @ u)*dt
        
        t = t + dt        
        lastTime = now        
        
    print('==> ', t, q[:2], np.rad2deg(q[2]))
    
    returnCode, pos = sim.simxGetObjectPosition(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)        
    print('Pos: ', pos)

    returnCode, ori = sim.simxGetObjectOrientation(clientID, robotHandle, -1, sim.simx_opmode_oneshot_wait)
    print('Ori: ', np.rad2deg(ori))
        
    sim.simxSetJointTargetVelocity(clientID, wheel1, 0, sim.simx_opmode_oneshot_wait)
    sim.simxSetJointTargetVelocity(clientID, wheel2, 0, sim.simx_opmode_oneshot_wait)
    sim.simxSetJointTargetVelocity(clientID, wheel3, 0, sim.simx_opmode_oneshot_wait)
        
    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
    
else:
    print ('Failed connecting to remote API server')
    
print ('Program ended')