import matplotlib.pyplot as plt
import numpy as np
# --------------------------------------------------------------------------
def Rz(theta):
    return np.array([[  np.cos(theta), -np.sin(theta), 0 ],
                      [ np.sin(theta),  np.cos(theta), 0 ],
                      [ 0            ,  0            , 1 ]])
# --------------------------------------------------------------------------
def calcularB(B, Borig, th):
    Rab = Rz(np.deg2rad(th))
    Tab = np.column_stack((Rab, Borig))
    aux = np.array([0, 0, 0, 1])
    Tab = np.row_stack((Tab, aux))
    A = Tab @ B
    return A
#------------------------------------------------------------------------------------
# Definindo os vetores
origin = np.array([[0, 2], [0, 3]])  # Origem dos vetores
vectors = np.array([[2, 1], [4, 0]])  # Coordenadas dos vetores
B = np.array([3, 1, 0, 1])
Borig = np.array([2, 3, 0])
A = calcularB(B, Borig, 90)
print(A)
# Plotando os vetores
plt.quiver(*origin, vectors[0], vectors[1], angles='xy', scale_units='xy', scale=1, color=['r', 'b'])
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Plotagem de Vetores 2D')
plt.grid(True)
plt.show()
