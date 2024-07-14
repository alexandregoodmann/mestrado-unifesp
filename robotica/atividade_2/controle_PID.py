import matplotlib.pyplot as plt

# u(t) = Kp * e(t)
# u(t) -> saída do controlador
# Kp   -> ganho proporcional
# e(t) -> erro no tempo t

# Parâmetros do controlador
Kp = 1.0

# parametros
begin = 0
actual = begin
setpoint = 100

# Plotar resultados
plt.plot(tempo, saida, label='Saída do Controlador P')
plt.xlabel('Tempo')
plt.ylabel('Saída')
plt.legend()
plt.show()
