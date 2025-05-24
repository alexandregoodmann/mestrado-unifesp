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

# Passo 3: Filtrar dados dos estados de Acre, Rio de Janeiro e Santa Catarina
acre_data = df[df['UF'] == 'AC']['Casos_novos_notificados']
rj_data = df[df['UF'] == 'RJ']['Casos_novos_notificados']
sc_data = df[df['UF'] == 'SC']['Casos_novos_notificados']

# Passo 4: Verificar a normalidade dos dados
# Teste de Shapiro-Wilk para Acre
stat_acre, p_value_acre = stats.shapiro(acre_data)
print(f"Normalidade do Acre: Estatística={stat_acre}, p-valor={p_value_acre}")

# Teste de Shapiro-Wilk para Rio de Janeiro
stat_rj, p_value_rj = stats.shapiro(rj_data)
print(f"Normalidade do Rio de Janeiro: Estatística={stat_rj}, p-valor={p_value_rj}")

# Teste de Shapiro-Wilk para Santa Catarina
stat_sc, p_value_sc = stats.shapiro(sc_data)
print(f"Normalidade de Santa Catarina: Estatística={stat_sc}, p-valor={p_value_sc}")

# Passo 5: Verificar a homogeneidade de variâncias (Teste de Levene)
stat_levene, p_value_levene = stats.levene(acre_data, rj_data, sc_data)
print(f"Homogeneidade de variâncias (Levene): Estatística={stat_levene}, p-valor={p_value_levene}")

# Passo 6: Realizar o teste ANOVA (se as suposições forem atendidas)
if p_value_acre > 0.05 and p_value_rj > 0.05 and p_value_sc > 0.05 and p_value_levene > 0.05:
    f_stat, p_value_anova = stats.f_oneway(acre_data, rj_data, sc_data)
    print(f"Resultado do teste ANOVA: Estatística F={f_stat}, p-valor={p_value_anova}")

    # Passo 7: Interpretar o valor-p da ANOVA
    if p_value_anova < 0.05:
        print("Há diferença significativa entre os estados.")
    else:
        print("Não há diferença significativa entre os estados.")
else:
    print("As suposições (normalidade e homogeneidade de variâncias) não foram atendidas.")
