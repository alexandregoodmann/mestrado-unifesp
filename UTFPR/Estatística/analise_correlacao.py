import pandas as pd
from scipy.stats import ttest_ind
import os

# Para Windows
os.system('cls')

# Carrega o arquivo CSV
df = pd.read_csv("country_emissions.csv")

# Filtra os dados dos dois países
btn = df[df['iso3_country'] == 'BTN']['emissions_quantity']
afg = df[df['iso3_country'] == 'AFG']['emissions_quantity']

# Teste t para duas amostras independentes
t_stat, p_val = ttest_ind(btn, afg, equal_var=False)  # Welch’s t-test

print(f"Estatística t: {t_stat}")
print(f"p-valor: {p_val}")

# Interpretação
if p_val < 0.01:
    print("Há diferença significativa (p < 0.01)")
elif p_val < 0.05:
    print("Há diferença significativa (p < 0.05)")
else:
    print("Não há diferença significativa")
