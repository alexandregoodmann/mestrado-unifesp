# --------------------------------------------------------------------------------
# Parte 4 — Polimorfismo e Composição
# --------------------------------------------------------------------------------

# Ex 7 — Animal: Animal.falar(); Cachorro e Gato sobrescrevem.
class Animal():
    def __init__(self):
        pass

    def emitir_som(self):
        return "Animal emite som"

class Gato(Animal):
    def __init__(self):
        pass

    def emitir_som(self):
        return "Gato faz miau"

class Cachorro(Animal):
    def __init__(self):
        pass

    def emitir_som(self):
        return 'Cachorro Late AU AU'

animal_1 = Animal()
animal_2 = Gato()
animal_3 = Cachorro()
print(animal_1.emitir_som())
print(animal_2.emitir_som())
print(animal_3.emitir_som())

# Ex 8 — Turma: Aluno (nome, nota); Turma agrega; métodos media(), aprovados(), reprovados().
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

class Turma:
    _alunos = []
    def __init__(self):
        pass
    
    def addALuno(self, aluno):
        self._alunos.append(aluno)

    def media(self):
        media = 0
        for aluno in self._alunos:
            media += aluno.nota
        media = media / len(self._alunos)
        return media
    
    def aprovados(self):
        aprovados = []
        for aluno in self._alunos:
            if (aluno.nota >= 7):
                aprovados.append(aluno)
        return aprovados
    
    def reprovados(self):
        reprovados = []
        for aluno in self._alunos:
            if (aluno.nota < 7):
                reprovados.append(aluno)
        return reprovados

# Faz um loop para criar 10 alunos com notas e adicionar na turma
turma = Turma()
for index in range(0, 10):
    aluno = Aluno(f"Aluno 0{str(index)}", index)
    turma.addALuno(aluno)

# Exibe todos aprovados, nota >= 7
aprovados = turma.aprovados()
for aprovado in aprovados:
    print(f"Aluno: {aprovado.nome}, foi APROVADO com media {aprovado.nota}")

# Exibe todos reprovados
reprovados = turma.reprovados()
for reprovado in reprovados:
    print(f"Aluno: {reprovado.nome}, foi REPROVADO com media {reprovado.nota}")


# Ex 9 — Carrinho: Produto e Carrinho (adicionar, total(), listar).
class Produto():
    item = ''
    valor = 0

    def __init__(self):
        pass

    def __str__(self):
        return f"{self.item} - valor: R$ {self.valor:,.2f}"

class Carrinho():
    produtos = []
    def __init__(self):
        pass

    def addProduto(self, produto):
        self.produtos.append(produto)

    def total(self):
        total = 0
        for item in self.produtos:
            total += item.valor
        return total
    
    def listar(self):
        for item in self.produtos:
            print(item)

#Cria 20 produtos e adiciona ao carrinho
carrinho = Carrinho()
for index in range(1, 21):
    produto = Produto()
    produto.item = f"Produto {index}"
    produto.valor = index * 1.35 + 2.35
    carrinho.addProduto(produto)

carrinho.listar()
print(f"Total do carrinho é: R$ {carrinho.total():,.2f}")