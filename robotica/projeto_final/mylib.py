import sim 
import math
import numpy as np

def pararSimulacao(clientID):
    
    # Parando a simulação     
    stop = sim.simxStopSimulation(clientID,sim.simx_opmode_blocking)         
    
    # Finaliza conexao com CoppeliaSim:
    finish = sim.simxFinish(clientID)
    print('stop', stop, finish)

    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)

# ---------------------------------------------------------------------------------------
def getAngulo(vetA, vetB):
    vet = vetB - vetA
    print(vet)
    ang = math.atan(vet[1]/vet[0])
    return np.rad2deg(ang)
# ---------------------------------------------------------------------------------------
'''
a = np.array([0, 0, 0])
b = np.array([30, -30, 30])
resp = getAngulo(a, b)
print(b, resp)
'''