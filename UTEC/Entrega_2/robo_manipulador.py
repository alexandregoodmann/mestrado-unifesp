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
    
class Componente3D(Componente2D):
    z_inicial = 0
    z_final = 0
    z_deslocamento = 0

    def __init__(self, nome, angulo=0, comprimento=5, limite_min=-180, limite_max=180):
        self.nome = nome
        self.angulo = angulo
        self.comprimento = comprimento
        self.limite_min = limite_min
        self.limite_max = limite_max

    def __str__(self):
        return f"{self.angulo, self.x_inicial, self.y_inicial, self.x_final, self.y_final}"

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

j1 = Componente2D('J1', 30, 30)
j2 = Componente2D('J2', 30, 20)
j3 = Componente2D('J3', -30, 12)

manipulador2D = Manipulador2D()
manipulador2D.addComponente(j1)
manipulador2D.addComponente(j2)
manipulador2D.addComponente(j3)
print('Posição Final: ', j3.x_final, j3.y_final)
manipulador2D.exibir_grafico2D()

class Manipulador3D(Manipulador2D):
    def __init__(self):
        super().__init__()
        self.

    