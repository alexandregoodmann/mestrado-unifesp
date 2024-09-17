# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Atividade Aula 05
# --------------------------------------------------------------------------------------

import random
import time
from datetime import datetime, timedelta

# --------------------------------------------------------------------------------------
# Função para gerar uma data aleatória entre duas datas
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# --------------------------------------------------------------------------------------
# Definindo intervalo de datas
start_date = datetime(2000, 1, 1)
end_date = datetime(2024, 12, 31)

# --------------------------------------------------------------------------------------
# Gerando 1000 datas aleatórias
random_dates = [(random_date(start_date, end_date)) for _ in range(1000)]
string_dates = []
for date in random_dates:
    string_dates.append(date.strftime("%Y-%m-%d"))

# --------------------------------------------------------------------------------------
# Função para extrair parte específica da data
def extract_date_part(date_str, part):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    if part == 'day':
        return date_obj.day
    elif part == 'month':
        return date_obj.month
    elif part == 'year':
        return date_obj.year


# --------------------------------------------------------------------------------------
# Função de Counting Sort (estável)
def counting_sort(dates, key_func, max_value):
    count = [0] * (max_value + 1)
    output = [None] * len(dates)
    
    # Contando a ocorrência de cada valor
    for date in dates:
        index = key_func(date)
        count[index] += 1
    
    # Acumulação dos valores
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Construindo a lista ordenada
    for date in reversed(dates):
        index = key_func(date)
        output[count[index] - 1] = date
        count[index] -= 1
    
    return output

# --------------------------------------------------------------------------------------
# Função Radix Sort com mistura de métodos estáveis e não estáveis
def radix_sort_dates_combined(dates):
    # Ordenar primeiro pelo dia (usando Counting Sort)
    dates = counting_sort(dates, key_func=lambda date: extract_date_part(date, 'day'), max_value=31)
    
    # Ordenar pelo mês (usando Counting Sort)
    dates = counting_sort(dates, key_func=lambda date: extract_date_part(date, 'month'), max_value=12)
    
    # Ordenar pelo ano (usando um método não estável - Quick Sort)
    dates.sort(key=lambda date: extract_date_part(date, 'year'))  # Quick Sort não é estável
    
    return dates

# --------------------------------------------------------------------------------------
# Ordenando as datas
start_time = time.time()

sorted_dates = radix_sort_dates_combined(string_dates)

end_time = time.time()
execution_time = end_time - start_time

# Exibindo o resultado
for date in sorted_dates:
    print(date)

print(f"Tempo de execução: {execution_time} segundos")