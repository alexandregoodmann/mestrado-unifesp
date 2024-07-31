import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Função para rotacionar um vetor em torno do eixo Z
def rotate_z(vector, angle):
    # Matriz de rotação em torno do eixo Z
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle),  np.cos(angle), 0],
        [0,             0,             1]
    ])
    # Aplicando a rotação ao vetor
    rotated_vector = np.dot(rotation_matrix, vector)
    return rotated_vector

# Definindo o vetor original
original_vector = np.array([3, 2, 1])

# Definindo o ângulo de rotação (em radianos)
angle = np.radians(60)  # Rotação de 45 graus

# Calculando o vetor rotacionado
rotated_vector = rotate_z(original_vector, angle)

# Plotando o vetor original e o rotacionado
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vetor original
ax.quiver(0, 0, 0, *original_vector, color='b', label='Vetor Original')

# Vetor rotacionado
ax.quiver(0, 0, 0, *rotated_vector, color='r', label='Vetor Rotacionado')

# Ajustando os limites dos eixos
ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.set_zlim([0, 5])

# Rótulos dos eixos
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

# Título e legenda
ax.set_title('Rotação de Vetor em Torno do Eixo Z')
ax.legend()

# Mostrando o gráfico
plt.show()
