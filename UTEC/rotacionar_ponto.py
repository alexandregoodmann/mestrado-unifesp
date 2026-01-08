import math
import plotly.graph_objects as go

def rotacionar_ponto(x, y, z, ang_x, ang_y, ang_z):
    ax, ay, az = map(math.radians, [ang_x, ang_y, ang_z])

    # Rotação em X
    yx = y * math.cos(ax) - z * math.sin(ax)
    zx = y * math.sin(ax) + z * math.cos(ax)
    x1, y1, z1 = x, yx, zx

    # Rotação em Y
    x2 = x1 * math.cos(ay) + z1 * math.sin(ay)
    y2 = y1
    z2 = -x1 * math.sin(ay) + z1 * math.cos(ay)

    # Rotação em Z
    x3 = x2 * math.cos(az) - y2 * math.sin(az)
    y3 = x2 * math.sin(az) + y2 * math.cos(az)
    z3 = z2

    return x3, y3, z3


# --- Vetor inicial (de origem até o ponto) ---
vetor = (1, 0, 0)  # eixo X

# --- Rotação ---
angulos = (0, 0, 90)
v_rot = rotacionar_ponto(*vetor, *angulos)

# --- Cria gráfico ---
fig = go.Figure()

# Vetor original (azul)
fig.add_trace(go.Scatter3d(
    x=[0, vetor[0]],
    y=[0, vetor[1]],
    z=[0, vetor[2]],
    mode='lines+markers+text',
    line=dict(color='blue', width=6),
    marker=dict(size=4, color='blue'),
    text=['', 'Vetor original'],
    textposition='top center'
))

# Vetor rotacionado (vermelho)
fig.add_trace(go.Scatter3d(
    x=[0, v_rot[0]],
    y=[0, v_rot[1]],
    z=[0, v_rot[2]],
    mode='lines+markers+text',
    line=dict(color='red', width=6),
    marker=dict(size=4, color='red'),
    text=['', 'Vetor rotacionado'],
    textposition='top center'
))

# --- Desenhar eixos de referência (XYZ) ---
eixos = {
    'X': ([0, 1], [0, 0], [0, 0], 'green'),
    'Y': ([0, 0], [0, 1], [0, 0], 'orange'),
    'Z': ([0, 0], [0, 0], [0, 1], 'purple'),
}

for nome, (x, y, z, cor) in eixos.items():
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode='lines+text',
        line=dict(color=cor, width=2),
        text=['', nome],
        textposition='top center'
    ))

# --- Layout ---
fig.update_layout(
    title=f"Rotação de vetor em 3D - X={angulos[0]}°, Y={angulos[1]}°, Z={angulos[2]}°",
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='cube',
        xaxis=dict(range=[-1.5, 1.5]),
        yaxis=dict(range=[-1.5, 1.5]),
        zaxis=dict(range=[-1.5, 1.5])
    )
)

fig.show()
