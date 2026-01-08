import numpy as np
import plotly.graph_objects as go
import math

# --- Criação dos vetores (usando arrays NumPy) ---
v1 = np.array([1, 2, 0])
v2 = np.array([2, 0, 1])

print("Vetor 1:", v1)
print("Vetor 2:", v2)

# --- Operações básicas ---
soma = v1 + v2
subtracao = v1 - v2
produto_escalar = np.dot(v1, v2)
produto_vetorial = np.cross(v1, v2)

# --- Norma (magnitude) e vetor unitário ---
norma_v1 = np.linalg.norm(v1)
v1_unitario = v1 / norma_v1

# --- Ângulo entre vetores ---
cos_theta = produto_escalar / (np.linalg.norm(v1) * np.linalg.norm(v2))
angulo_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))
angulo_graus = np.degrees(angulo_rad)

print("\nSoma:", soma)
print("Subtração:", subtracao)
print("Produto escalar:", produto_escalar)
print("Produto vetorial:", produto_vetorial)
print("Norma de v1:", norma_v1)
print("Vetor unitário de v1:", v1_unitario)
print("Ângulo entre v1 e v2 (graus):", angulo_graus)

# --- Visualização com Plotly ---
# Criar gráfico 3D mostrando os vetores
fig = go.Figure()

# Adiciona o vetor v1
fig.add_trace(go.Scatter3d(
    x=[0, v1[0]], y=[0, v1[1]], z=[0, v1[2]],
    mode='lines+markers',
    line=dict(color='blue', width=6),
    name='v1'
))

# Adiciona o vetor v2
fig.add_trace(go.Scatter3d(
    x=[0, v2[0]], y=[0, v2[1]], z=[0, v2[2]],
    mode='lines+markers',
    line=dict(color='red', width=6),
    name='v2'
))

# Adiciona o vetor soma
fig.add_trace(go.Scatter3d(
    x=[0, soma[0]], y=[0, soma[1]], z=[0, soma[2]],
    mode='lines+markers',
    line=dict(color='green', width=4, dash='dash'),
    name='v1 + v2'
))

# Ajustes de layout
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ),
    title="Manipulação de Vetores 3D com NumPy e Plotly"
)

fig.show()
