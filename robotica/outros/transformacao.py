import numpy as np
import matplotlib.pyplot as plt
import os
os.system('cls' if os.name == 'nt' else 'clear')

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
# --------------------------------------------------------------------------
# Apenas para visualização de um referencial no plano
def plot_frame(Porg, R, c=['r', 'g']):
    axis_size = 3.0    
    axes = axis_size*R
    x_axis = np.array(axes[0:2,0])
    y_axis = np.array(axes[0:2,1])
    # X
    plt.quiver(*Porg[:2], *x_axis, color=c[0], angles='xy', scale_units='xy', scale=1)
    # Y
    plt.quiver(*Porg[:2], *y_axis, color=c[1], angles='xy', scale_units='xy', scale=1)
# --------------------------------------------------------------------------

B = np.array([3, 7, 0, 1])
Borig = np.array([10, 5, 0])

'''
AA = calcularB(B, Borig, 30)
print(AA)
exit()
'''
Rab = Rz(np.deg2rad(0))
print('Rab', Rab)
# Concatena o vetor origem ao final (coluna)
Tab = np.column_stack((Rab, Borig))

# Concatena o vetor auxiliar embaixo (linha)
aux = np.array([0, 0, 0, 1])
Tab = np.row_stack((Tab, aux))
print('Tab', Tab)
A = Tab @ B
print('A', A)
# -----------------------------------------------------------------------

# Plotando os referenciais
plt.figure()
plot_frame(Borig, Rab, ['g', 'g'])

# Vetor Pa_borg
pa_org = np.array([0, 0])
plt.quiver(*pa_org[:2], *Borig[:2], color='g', angles='xy', scale_units='xy', scale=1)

# Vetor Pb
pb_aux = Rab @ B[:3]
plt.quiver(*Borig[:2], *pb_aux[:2], color='g', angles='xy', scale_units='xy', scale=1)

# Vetor Pa
plt.quiver(*pa_org[:2], *A[:2], color='b', angles='xy', scale_units='xy', scale=1)

plt.plot(A[0], A[1], 'o', color='b')

plt.axis('scaled')
plt.axis((0, 14, 0, 14))
plt.show()