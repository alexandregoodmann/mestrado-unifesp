# --------------------------------------------------------------------------------------
# UTEC - Especialização em Robótica e Inteligência Artificial
# Disciplina: Programação Básica
# Aluno: Alexandre Ferreira e Silva
# Atividade 02
# --------------------------------------------------------------------------------------

import math

class Junta:
    def __init__(self, nome, angulo=0, limite_min=-180, limite_max=180):
        self.nome = nome
        self.angulo = angulo
        self.limite_min = limite_min
        self.limite_max = limite_max

    def mover(self, novo_angulo):
        if self.limite_min <= novo_angulo <= self.limite_max:
            self.angulo = novo_angulo
            print(f"Junta {self.nome} movida para {self.angulo}°")
        else:
            print(f"Movimento inválido para {self.nome}! Fora dos limites.")

class Elo:
    def __init__(self, comprimento):
        self.comprimento = comprimento

class Manipulador:
    def __init__(self, nome):
        self.nome = nome
        self.juntas = []
        self.elos = []

    def adicionar_junta(self, junta):
        self.juntas.append(junta)

    def adicionar_elo(self, elo):
        self.elos.append(elo)

    def mover_junta(self, indice, angulo):
        if 0 <= indice < len(self.juntas):
            self.juntas[indice].mover(angulo)

    def status(self):
        print(f"Manipulador {self.nome}:")
        for i, j in enumerate(self.juntas):
            print(f"  Junta {i} ({j.nome}): {j.angulo}°")
        for i, e in enumerate(self.elos):
            print(f"  Elo {i}: {e.comprimento} unidades")

    def calcular_posicao_final(self):
        """Cinemática direta simples para manipulador planar 2D."""
        x, y, angulo_total = 0.0, 0.0, 0.0
        for junta, elo in zip(self.juntas, self.elos):
            angulo_total += math.radians(junta.angulo)
            x += elo.comprimento * math.cos(angulo_total)
            y += elo.comprimento * math.sin(angulo_total)
        return (x, y)

# Exemplo de uso
if __name__ == "__main__":
    j1 = Junta("Base", 0, -90, 90)
    j2 = Junta("Cotovelo", 0, -135, 135)

    e1 = Elo(5)
    e2 = Elo(3)

    robo = Manipulador("Robo2D")
    robo.adicionar_junta(j1)
    robo.adicionar_elo(e1)
    robo.adicionar_junta(j2)
    robo.adicionar_elo(e2)

    robo.status()
    robo.mover_junta(0, 45)
    robo.mover_junta(1, 60)
    print("Posição final do efetuador:", robo.calcular_posicao_final())