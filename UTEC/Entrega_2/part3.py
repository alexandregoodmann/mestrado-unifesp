# --------------------------------------------------------------------------------
# Parte 3 — Herança
# --------------------------------------------------------------------------------

# Ex 5 — Veículo: superclasse Veiculo (marca, modelo), subclasses Carro e Moto com tipo().
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo):
    __tipo = ''
    def __init__(self):
        pass
    def __str__(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Modelo: {self.modelo}"

class Moto(Veiculo):
    __tipo = ''
    def __init__(self):
        pass
    def __str__(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Modelo: {self.modelo}"

veiculo1 = Carro()
veiculo1.marca = 'Volkswagen'
veiculo1.modelo = 'Tiguan'
veiculo1.tipo = 'Carro'

veiculo2 = Moto()
veiculo2.marca = 'Honda'
veiculo2.modelo = 'Twister'
veiculo2.tipo = 'Moto'

print(str(veiculo1))
print(str(veiculo2))

# Ex 6 — Funcionário/Gerente: Funcionario (nome, salário) e Gerente (+20%); lista mista e folha de pagamento.

class Funcionario:
    nome = ''
    salario = 0
    def __init__(self):
        pass

    def __str__(self):
        return f"Funcionário: {self.nome}, Salário: {self.salario}"

class Gerente(Funcionario):
    def __init__(self):
        pass

    def getSalario(self):
        return self.salario * 1.2
    
    def __str__(self):
        salario = self.salario*1.2
        return f"Gerente: {self.nome}, Salário: {self.getSalario()}"

salariobase = 12000
funcionario1 = Funcionario()
funcionario1.nome = 'Alexandre'
funcionario1.salario = salariobase

funcionario2 = Gerente()
funcionario2.nome = 'Ferreira'
funcionario2.salario = salariobase

print(str(funcionario1))
print(str(funcionario2))