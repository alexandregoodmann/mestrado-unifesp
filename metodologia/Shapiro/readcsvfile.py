import csv
import os

#limpar console
os.system('cls' if os.name == 'nt' else 'clear')

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            data.append(row)
    return data

# Example usage:
file_path = '/home/alexandre/Documents/robotica/aula2/estatistica/regiao.csv'  # Replace 'example.csv' with your CSV file path
csv_data = read_csv_file(file_path)

#nome das colunas
print(csv_data[0])

#primeira 5 linhas
for linha in csv_data[1:5]:
    print(linha[0], linha[6])

#print(csv_data[1:5])
