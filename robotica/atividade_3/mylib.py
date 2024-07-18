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
def getFuncaoReta(origem, destino):
    x = np.array([origem[0], destino[0]])
    y = np.array([origem[1], destino[1]])
    coefficients = np.polyfit(x, y, 1)
    a, b = coefficients
    print(f"Equação da linha ajustada: y = {a:.2f}x + {b:.2f}")
    return a, b

def isOnLine(x, y, a, b):
    fx = a*x + b
    inf = fx - 0.1
    sup = fx + 0.1
    if (y >= inf and y <= sup):
        return True
    return False
'''
origem = np.array([1, 2])
destino = np.array([3, 4])
a, b = getFuncaoReta(origem, destino)

print(isOnLine(1.5, 2.5))
'''
# ---------------------------------------------------------------------------------------
