import plotly.graph_objects as go

# Vetor 3D
vx, vy, vz = 0, 10, 15  # vetor (2,3,4)

fig = go.Figure()

# Linha do vetor
fig.add_trace(go.Scatter3d(x=[0, vx], y=[0, vy], z=[0, vz],
                           mode="lines+markers",
                           line=dict(width=6, color="blue"),
                           marker=dict(size=4, color="red")))

# Adiciona seta (aproximação com anotação 3D não existe direto)
# Aqui simulamos a ponta do vetor com um ponto extra
fig.add_trace(go.Scatter3d(x=[vx], y=[vy], z=[vz],
                           mode="markers",
                           marker=dict(size=6, color="blue", symbol="diamond")))

# Configuração dos eixos
fig.update_layout(scene=dict(
    xaxis=dict(range=[0, 20]),
    yaxis=dict(range=[0, 20]),
    zaxis=dict(range=[0, 20])),
    title="Exemplo de Vetor 3D com Plotly"
)

fig.show()
