import pandas as pd
from scipy import stats
import numpy as np
import os

# Para Windows
os.system('cls')

# Passo 1: Carregar os dados do arquivo Excel
# Substitua o caminho pelo local do seu arquivo 'Notificacoes.xlsx'
df = pd.read_csv('Notificacoes.csv', low_memory=False)

# Passo 2: Substituir valores ausentes por 0
df = df.fillna(0)

# Passo 3: Filtrar dados dos estados de Mato Grosso e São Paulo
matogrosso_data = df[df['UF'] == 'MT']['Casos_novos_notificados']
print(matogrosso_data.head())

saopaulo_data = df[df['UF'] == 'SP']['Casos_novos_notificados']
print(saopaulo_data.head())


# Passo 4: Verificar a normalidade dos dados
# Teste de Shapiro-Wilk para Mato Grosso
stat_mt, p_value_mt = stats.shapiro(matogrosso_data)
print(f"Normalidade de Mato Grosso: Estatística={stat_mt}, p-valor={p_value_mt}")

# Teste de Shapiro-Wilk para São Paulo
stat_sp, p_value_sp = stats.shapiro(saopaulo_data)
print(f"Normalidade de São Paulo: Estatística={stat_sp}, p-valor={p_value_sp}")

# Passo 5: Realizar o teste t para duas amostras independentes
# Supondo que os dados sejam normais (p-valor > 0.05 para o teste de Shapiro-Wilk)
t_stat, p_value_ttest = stats.ttest_ind(matogrosso_data, saopaulo_data)

print(f"Resultado do teste t: Estatística t={t_stat}, p-valor={p_value_ttest}")

# Passo 6: Interpretar o valor-p
if p_value_ttest < 0.05:
    print("Há diferença significativa entre os estados.")
else:
    print("Não há diferença significativa entre os estados.")
