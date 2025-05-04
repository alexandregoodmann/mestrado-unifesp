import pandas as pd
import random

# Configurações para geração dos dados
num_linhas = 100

contas = [f"C{str(i).zfill(4)}" for i in range(1, num_linhas + 1)]
rendas = [round(random.uniform(1000, 10000), 2) for _ in range(num_linhas)]
dividas = [round(random.uniform(0, 8000), 2) for _ in range(num_linhas)]

classes = []
for i in range(0,100):
    classe = dividas[i] / rendas[i]
    if (classe >= 0.3):
        classes.append('bom')
    else:
       classes.append('ruim')

# Criar DataFrame
dados = {
    "Conta":contas,
    "Renda": rendas,
    "Dívida": dividas,
    "Classe": classes
}
df = pd.DataFrame(dados)

# Salvar em um arquivo CSV
df.to_csv("Bloco1_Tarefa1\dados_contas.csv", index=False)
