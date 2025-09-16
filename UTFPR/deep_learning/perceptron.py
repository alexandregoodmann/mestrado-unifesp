import numpy as np
import random as r

tabela = np.array([
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 1]])

def perceptron(entrada):
    soma = 0
    peso = [6, 5, 2]
    for i in range(0, 3):
        soma += entrada[i] * peso[i]
    print(soma)
    if (soma > 8):
        return 1
    else:
        return 0


resultado = []
for i in range(0, tabela.__len__()):
    resultado.append(perceptron(tabela[i][:3]))

print(resultado)