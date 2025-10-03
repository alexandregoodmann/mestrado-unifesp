# --------------------------------------------------------------------------------------
# UTEC - Especialização em Robótica e Inteligência Artificial
# Disciplina: Programação Básica
# Aluno: Alexandre Ferreira e Silva
# Atividade 02
# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------
# Classe para manipular um robô 2D com demonstração gráfica
# Serve para vários elementos (elos e juntas)
# No momento de adicionar um elemento no manipulador, já calcula todos os parâmetros considerando a posição do anterior
# --------------------------------------------------------------------------------------

import math
import plotly.graph_objects as go

class Manipulador3D():
    componentes = []
    def __init__(self):
        pass

    def addComponent(self, componente):
        tamanho = self.componentes.__len__()
        if (tamanho == 0):
            gama = componente.gama
            theta = componente.theta
            h = componente.comprimento * math.cos(math.radians(componente.gama))
            x = h * math.cos(math.radians(componente.theta))
            y = h * math.sin(math.radians(componente.theta))
            z = componente.comprimento * math.sin(math.radians(componente.gama))
        else:
            anterior = self.componentes[tamanho - 1]
            gama = componente.gama + anterior.gama
            theta = componente.theta + anterior.theta
            h = componente.comprimento * math.cos(math.radians(gama))
            x = anterior.x + h * math.cos(math.radians(theta))
            y = anterior.y + h * math.sin(math.radians(theta))
            z = anterior.z + componente.comprimento * math.sin(math.radians(gama))
        
        componente.gama = gama
        componente.theta = theta
        componente.x = x
        componente.y = y
        componente.z = z
        print('Componente 3D: ', componente)
        self.componentes.append(componente)

    def exibirGrafico3D(self):
        fig = go.Figure()

        for index, item in enumerate(self.componentes):
            if index == 0:
                fig.add_trace(go.Scatter3d(x=[0, item.x], y=[0, item.y], z=[0, item.z], mode="lines+markers", line=dict(width=6, color="blue"), marker=dict(size=4, color="red")))
            else:
                anterior = self.componentes[index - 1]
                fig.add_trace(go.Scatter3d(x=[anterior.x, item.x], y=[anterior.y, item.y], z=[anterior.z, item.z], mode="lines+markers", line=dict(width=6, color="blue"), marker=dict(size=4, color="red")))

        fig.update_layout(scene=dict(
            xaxis=dict(range=[0, 60]),
            yaxis=dict(range=[0, 60]),
            zaxis=dict(range=[0, 60])),
            title="Exemplo de Vetor 3D com Plotly"
        )
        fig.show()