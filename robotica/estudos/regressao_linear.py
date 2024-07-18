import numpy as np
import matplotlib.pyplot as plt
import os

os.system('cls' if os.name == 'nt' else 'clear')

# Coordenadas conhecidas
x = np.array([-2.72, -3])
y = np.array([-1.34, 4])
vet = np.array([2, 3])
erro = 0.05
# Ajuste da linha usando polyfit (polinômio de grau 1)
coefficients = np.polyfit(x, y, 1)
m, b = coefficients

# Função linear
def linear_function(x):
    print(m, b)
    return m * x + b

# Valores ajustados
y_fit = linear_function(x)

yn = linear_function(vet[0])
ysup = yn + erro
yinf = yn - erro
if (vet[1] >= yinf and vet[1] <= ysup):
    print('Posicao linha', vet)
else:
    print('vetor nao esta na linha')

# Visualização
plt.scatter(x, y, label='Pontos conhecidos')
plt.scatter(vet[0], vet[1], label='Ponto')
plt.plot(x, y_fit, label='Linha ajustada', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

print(f"Equação da linha ajustada: y = {m:.2f}x + {b:.2f}")
