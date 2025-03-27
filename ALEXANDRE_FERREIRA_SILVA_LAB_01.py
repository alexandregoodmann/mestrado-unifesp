import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)
fig, ax = plt.subplots()
ax.plot(t, s)
ax.set_xlabel('Tempo')
ax.set_ylabel('Quantidade')
ax.set_title('Exponencial Decrescente')
ax.grid(True)
plt.show()
