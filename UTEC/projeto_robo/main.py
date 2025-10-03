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

import os
from robo_model import Componente2D, Componente3D
from manipulador2D_service import Manipulador2D
from manipulador3D_service import Manipulador3D

#limpar console
os.system('cls' if os.name == 'nt' else 'clear')

# --------------------------------------------------------------------------------------
# Criando componente 2D
# --------------------------------------------------------------------------------------
j1 = Componente2D('J1', 30, 30)
j2 = Componente2D('J2', 30, 20)
j3 = Componente2D('J3', -30, 12)

manipulador2D = Manipulador2D()
manipulador2D.addComponente(j1)
manipulador2D.addComponente(j2)
manipulador2D.addComponente(j3)
print('Posição Final: ', j3.x_final, j3.y_final)

manipulador2D.exibir_grafico2D()   

# --------------------------------------------------------------------------------------
# Criando componente 3D
# --------------------------------------------------------------------------------------
j3d_1 = Componente3D('J3D1', 45, 45, 30)
j3d_2 = Componente3D('J3D2', 0, -45, 20)
j3d_3 = Componente3D('J3D3', 0, 45, 10)

manipulador3D = Manipulador3D()
manipulador3D.addComponent(j3d_1)
manipulador3D.addComponent(j3d_2)
manipulador3D.addComponent(j3d_3)
manipulador3D.exibirGrafico3D()