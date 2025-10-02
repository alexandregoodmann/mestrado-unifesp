# --------------------------------------------------------------------------------------
# UTEC - Especialização em Robótica e Inteligência Artificial
# Disciplina: Programação Básica
# Aluno: Alexandre Ferreira e Silva
# Atividade 02
# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# Parte 1 — Conceitos Básicos (Classe e Objeto)
# --------------------------------------------------------------------------------

# Ex 1 — Retângulo: classe Retangulo com largura, altura, métodos area() e perimetro().
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2*(self.largura + self.altura)
    
ret = Retangulo(2, 3)
print('Area do retangulo: ', ret.area())
print('Perimetro do retangulo: ', ret.perimetro())

# Ex 2 — Conta Bancária: classe Conta com titular, saldo, métodos depositar() e sacar() (validar saldo).
class ContaBancaria:
    saldo = 0
    def __init__(self, titular):
        self.titular = titular

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if self.saldo < valor:
            return 'Saldo insuficiente'
        self.saldo -= valor
        return self.saldo
    
conta = ContaBancaria("Alexandre Ferreira")
saldo = conta.depositar(10)
print(conta.titular + ' - Saldo: ', saldo)

saldo = conta.sacar(5)
print(conta.titular + ' - Saldo: ', saldo)

saldo = conta.sacar(10)
print(conta.titular + ' - Saldo: ', saldo)
        

    