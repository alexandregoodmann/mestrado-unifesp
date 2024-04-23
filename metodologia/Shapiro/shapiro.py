import pandas as pd
import os
import numpy as np
from scipy.stats import shapiro
import matplotlib.pyplot as plt

# limpar console e prepara os dados
os.system('cls' if os.name == 'nt' else 'clear')
dados = pd.read_csv('/home/alexandre/projetos/mestrado-unifesp/Metodologia-Cientifica/Shapiro/regiao2.csv')
dataframe = pd.DataFrame({'ano':dados.ano, 'rendimento':dados.indicador_rendimento})

# 1. Pega os indicadores de rendimentos ordenados e prepara os numeros basicos
#indicadores = dados.indicador_rendimento.sort_values()
indicadores = dados.nota_saeb_matematica.sort_values()
#print(dados.groupby('ano').nota_saeb_matematica.nunique())
#exit()

plt.hist(indicadores)
plt.show()

static, p = shapiro(indicadores)
print(static, p)

exit()

n = indicadores.__len__() # numero de indicadores
X = indicadores.mean() # a media dos indicadores

# 2. Calcula o valor estático D
D = 0
for i in indicadores:
    D = D + pow(abs((i - X)), 2)

# 3. Calcula o valor estatico W
k = int(n/2)
soma = 0
a = 0 # esse valor vem da tabela
for i in range(1,k):
    soma = soma + a*(pow(X,(n-i+1)) - pow(X,i))
W = (1/D) * pow(soma, 2) 

print(W)

'''
# 1. Obter dados ordenados


# 2. 
desvio_padrao = np.std(dataframe.rendimento)
print(desvio_padrao)
print("Numero amostras: ", dataframe.__len__)

print(dados['ano'].unique())

print(dados.ano.max())

print('De %s ate %s' % (dados.ano.min(), dados.ano.max()))

print(dados['ano'].value_counts())

tabela1 = pd.crosstab(dados.ano, dados.indicador_rendimento)
print(tabela1)

'''