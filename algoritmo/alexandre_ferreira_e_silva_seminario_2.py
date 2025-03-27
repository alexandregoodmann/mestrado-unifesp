# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Seminário 2 Hash Tree
# Fonte: ChatGPT, Google Gemini
# --------------------------------------------------------------------------------------

import os
import hashlib
from tabulate import tabulate # >>>>>> pip install tabulate 
os.system('cls' if os.name == 'nt' else 'clear')


# Função para calcular o hash de um dado usando SHA-256
def hash_data(data):
    print('valor de data---->>>>', data)
    hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
    print(data, '-> ' + hash)
    return hash

# Classe para representar uma Hash Tree
class HashTree:
    def __init__(self, data_blocks):
        self.leaves = [hash_data(data) for data in data_blocks]
        self.root = self.build_tree(self.leaves)
    
    def build_tree(self, nodes):
        # Caso base: se houver apenas um nó, retornamos esse nó como a raiz
        if len(nodes) == 1:
            return nodes[0]
        
        # Caso contrário, iteramos em pares e calculamos os hashes dos pares
        new_level = []
        for i in range(0, len(nodes), 2):
            # Se houver um nó sem par, ele é promovido para o próximo nível
            if i + 1 < len(nodes):
                combined_hash = hash_data(nodes[i] + nodes[i + 1])
            else:
                combined_hash = nodes[i]
            new_level.append(combined_hash)
        
        # Chamamos recursivamente até restar apenas a raiz
        return self.build_tree(new_level)
    
    def get_root(self):
        return self.root

# Exemplo de uso
data_blocks = ["bloco A", "bloco B", "bloco C", "bloco D"]
tree = HashTree(data_blocks)
print("RAIZ", tree.get_root())
