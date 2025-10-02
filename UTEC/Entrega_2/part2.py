# --------------------------------------------------------------------------------------
# UTEC - Especialização em Robótica e Inteligência Artificial
# Disciplina: Programação Básica
# Aluno: Alexandre Ferreira e Silva
# Atividade 02
# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# Parte 2 — Encapsulamento e Métodos Especiais
# --------------------------------------------------------------------------------

# Ex 3 — Produto: atributos privados _nome, _preco; método de desconto (%); implementar __str__.
class Produto:

    def __init__(self, nome, preco, desconto):
        self._nome = nome
        self._preco = preco
        self._desconto = desconto

    def __str__(self):
        valor = self._preco * (100 - self._desconto)/100
        return f"{self._nome} pagará o valor de {valor}. Aplicado {self._desconto}% de desconto"
    
produ = Produto('Alexandre', 1000, 10)
print(str(produ))

# Ex 4 — Aluno (com propriedades): @property para restringir nota entre 0 e 10; método aprovado().
class Aluno:
    __nota = 0
    def __init__(self):
        pass 

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        if nota < 0 or nota > 10:
             raise ValueError('A nota deverá estar entre 0 e 10')
        self.__nota = nota

    def aprovado(self):
        if self.__nota > 7:
            return True
        else:
            return False

aluno = Aluno()
# este try foi colocado para demonstrar o tratamento de exception e para seguir o código
try:
    aluno.nota = 30
    print('Aluno aprovado: ', aluno.aprovado())
except ValueError:
    print('Valor da nota deverá ser entre 0 e 10')

aluno.nota = 4
print('Aluno aprovado: ', aluno.aprovado())

aluno.nota = 9
print('Aluno aprovado: ', aluno.aprovado())