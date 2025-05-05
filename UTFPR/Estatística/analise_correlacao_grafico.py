import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o CSV
df = pd.read_csv("country_emissions.csv")

# Filtrar dados de BTN e AFG
df_filtered = df[df['iso3_country'].isin(['BTN', 'AFG'])]

# --- Boxplot ---
plt.figure(figsize=(8, 5))
sns.boxplot(x='Country', y='Emissions', data=df_filtered)
plt.title('Boxplot das Emissões: BTN vs AFG')
plt.ylabel('Emissões')
plt.xlabel('País')
plt.grid(True)
plt.show()

# --- Histograma ---
plt.figure(figsize=(8, 5))
sns.histplot(data=df_filtered, x='Emissions', hue='Country', kde=True, bins=20)
plt.title('Distribuição das Emissões: BTN vs AFG')
plt.xlabel('Emissões')
plt.grid(True)
plt.show()
