import pandas as pd
import os

# Para Windows
os.system('cls')

# Carrega o arquivo CSV
df = pd.read_csv('Notificacoes.csv', low_memory=False)

# Visualiza as primeiras linhas (opcional)



# Filtra os dados para o estado de São Paulo (UF == 'SP')
df_sp = df[df['UF'] == 'SP']
print(df_sp.head())

# Calcula o desvio padrão da coluna de casos novos notificados
desvio_padrao = df_sp['Casos_novos_notificados'].std()
print(f'Desvio padrão dos casos novos notificados em SP: {desvio_padrao}')
