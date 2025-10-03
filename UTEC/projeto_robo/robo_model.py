# --------------------------------------------------------------------------------------
# UTEC - Especialização em Robótica e Inteligência Artificial
# Disciplina: Programação Básica
# Aluno: Alexandre Ferreira e Silva
# Atividade 02
# --------------------------------------------------------------------------------------

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