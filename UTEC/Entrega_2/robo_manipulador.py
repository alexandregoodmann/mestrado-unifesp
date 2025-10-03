# --------------------------------------------------------------------------------------
# UTEC - Especialização em Robótica e Inteligência Artificial
# Disciplina: Programação Básica
# Aluno: Alexandre Ferreira e Silva
# Atividade 02
# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------
# Exercício para os alunos: Crie subclasses Manipulador2D (planar) e Manipulador3D (espacial) a partir da classe Manipulador, implementando o cálculo da posição final em cada caso.
# © Especialização em Robótica e IA — Materiais didáticos POO em Python Los que NO tengan accesso al Moodle hasta la fecha limite de entrega, DEBEN enviar sus soluciones a mi
# correo: andre.dasilva@utec.edu.uySlds
# --------------------------------------------------------------------------------------

import math
import matplotlib.pyplot as plt
import os
import plotly.graph_objects as go

#limpar console
os.system('cls' if os.name == 'nt' else 'clear')

# --------------------------------------------------------------------------------------
# Eu subistitui as classes de exemplo e criei somente uma que representa o elo e a junta
# --------------------------------------------------------------------------------------
class Componente2D:
    x_inicial = 0
    y_inicial = 0
    x_final = 0
    y_final = 0
    x_deslocamento = 0
    y_deslocamento = 0

    def __init__(self, nome, angulo=0, comprimento=5, limite_min=-180, limite_max=180):
        self.nome = nome
        self.angulo = angulo
        self.comprimento = comprimento
        self.limite_min = limite_min
        self.limite_max = limite_max

    def __str__(self):
        return f"{self.angulo, self.x_inicial, self.y_inicial, self.x_final, self.y_final}"
    
class Componente3D():
    x = 0
    y = 0
    z = 0
    def __init__(self, nome, theta=0, gama=0, comprimento=5):
        self.nome = nome
        self.theta = theta
        self.gama = gama
        self.comprimento = comprimento

    def __str__(self):
        return f"{self.theta, self.gama, self.x, self.y, self.z}"

# --------------------------------------------------------------------------------------
# Classe para manipular um robô 2D com demonstração gráfica
# Serve para vários elementos (elos e juntas)
# No momento de adicionar um elemento no manipulador, já calcula todos os parâmetros considerando a posição do anterior
# --------------------------------------------------------------------------------------
class Manipulador2D:
    componentes = []
    def __init__(self):
        pass

    def addComponente(self, componente):
        if (self.componentes.__len__() == 0): # se for o primeiro elemento da lista
            componente.x_final = math.cos(math.radians(componente.angulo)) * componente.comprimento
            componente.y_final = math.sin(math.radians(componente.angulo)) * componente.comprimento
            componente.x_deslocamento = componente.x_final
            componente.y_deslocamento = componente.y_final
        else:
            anterior = self.componentes[self.componentes.__len__() - 1] # pega o elemento anterior da lista
            componente.angulo = anterior.angulo + componente.angulo
            componente.x_inicial = anterior.x_final # o x inicial deste vetor é o final do anterior
            componente.y_inicial = anterior.y_final
            componente.x_deslocamento = math.cos(math.radians(componente.angulo)) * componente.comprimento # o x final deste vetor é o final do anterior + seu componente x
            componente.y_deslocamento = math.sin(math.radians(componente.angulo)) * componente.comprimento
            componente.x_final = componente.x_inicial + componente.x_deslocamento
            componente.y_final = componente.y_inicial + componente.y_deslocamento
        print('add componente', componente)
        self.componentes.append(componente)

    def exibir_grafico2D(self):

        if (self.componentes.__len__() == 0):
            raise ValueError("[ERROR] - Adicione componentes usando o método addComponente()")
        
        plt.figure(figsize=(6, 6)) # Define o tamanho da figura
        for item in self.componentes:
            plt.quiver(item.x_inicial, item.y_inicial, item.x_deslocamento, item.y_deslocamento, angles='xy', scale_units='xy', scale=1)

        plt.xlim([0, 50]) # Limites do eixo X
        plt.ylim([0, 50]) # Limites do eixo Y
        plt.xlabel("Eixo X")
        plt.ylabel("Eixo Y")
        plt.title("Posição do Robo")
        plt.grid(True)
        plt.axhline(0, color='black', linewidth=0.5) # Eixo X
        plt.axvline(0, color='black', linewidth=0.5) # Eixo Y
        plt.gca().set_aspect('equal', adjustable='box') # Garante que a escala seja igual para os eixos
        plt.show()

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

j1 = Componente2D('J1', 30, 30)
j2 = Componente2D('J2', 30, 20)
j3 = Componente2D('J3', -30, 12)

manipulador2D = Manipulador2D()
manipulador2D.addComponente(j1)
manipulador2D.addComponente(j2)
manipulador2D.addComponente(j3)
print('Posição Final: ', j3.x_final, j3.y_final)
#manipulador2D.exibir_grafico2D()   

j3d_1 = Componente3D('J3D1', 45, 45, 30)
j3d_2 = Componente3D('J3D2', 0, -45, 20)
j3d_3 = Componente3D('J3D3', 0, 45, 10)

manipulador3D = Manipulador3D()
manipulador3D.addComponent(j3d_1)
manipulador3D.addComponent(j3d_2)
manipulador3D.addComponent(j3d_3)
manipulador3D.exibirGrafico3D()