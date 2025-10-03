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