import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo
x = np.linspace(0, 10, 100)

# ==========================================
# JANELA 1 - Gráficos de Seno
# ==========================================
fig1 = plt.figure(1) # Cria ou ativa a primeira janela
fig1.suptitle('Janela 1: Funções Seno')

ax1 = fig1.add_subplot(2, 1, 1) # 2 linhas, 1 col, fig 1
ax1.plot(x, np.sin(x), 'r')
ax1.set_title('Seno')

ax2 = fig1.add_subplot(2, 1, 2) # 2 linhas, 1 col, fig 2
ax2.plot(x, np.sin(2 * x), 'b')
ax2.set_title('Seno Duplo')

# ==========================================
# JANELA 2 - Gráficos de Cosseno
# ==========================================
fig2 = plt.figure(2) # Cria ou ativa a segunda janela
fig2.suptitle('Janela 2: Funções Cosseno')

ax3 = fig2.add_subplot(1, 2, 1) # 1 linha, 2 col, fig 1
ax3.plot(x, np.cos(x), 'g')
ax3.set_title('Cosseno')

ax4 = fig2.add_subplot(1, 2, 2) # 1 linha, 2 col, fig 2
ax4.plot(x, np.cos(2 * x), 'y')
ax4.set_title('Cosseno Duplo')

# Ajusta o layout para não sobrepor títulos
plt.tight_layout()

# Exibe as janelas
plt.show()
