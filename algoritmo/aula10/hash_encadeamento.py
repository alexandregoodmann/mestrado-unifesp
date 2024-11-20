
class HashEncadeamento:
    def __init__(self, size):
        # Inicializa a tabela hash com listas vazias para encadeamento
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        # Função hash da divisão
        return key % self.size
    
    def insert(self, key, value):
        # Calcula o índice usando a função hash
        index = self.hash_function(key)
        # Insere o par chave-valor na lista encadeada no índice calculado
        self.table[index].append((key, value))
    
    def search(self, key):
        # Calcula o índice usando a função hash
        index = self.hash_function(key)
        # Percorre a lista encadeada para encontrar o valor correspondente à chave
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Retorna None se a chave não for encontrada
    
    def delete(self, key):
        # Calcula o índice usando a função hash
        index = self.hash_function(key)
        # Percorre a lista encadeada para encontrar e remover o par chave-valor
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True  # Retorna True se a chave foi encontrada e removida
        return False  # Retorna False se a chave não for encontrada
    
    def display(self):
        # Exibe o conteúdo da tabela hash
        for i, bucket in enumerate(self.table):
            print(f"Índice {i}: {bucket}")
'''

# Exemplo de uso
hash_table = HashEncadeamento(11)  # Cria uma tabela hash com 11 posições

# Inserção de pares chave-valor
hash_table.insert(10, "Valor para chave 10")
hash_table.insert(22, "Valor para chave 22")
hash_table.insert(31, "Valor para chave 31")
hash_table.insert(4, "Valor para chave 4")
hash_table.insert(15, "Valor para chave 15")

# Exibe a tabela hash
hash_table.display()

# Busca de uma chave
print("Busca pela chave 22:", hash_table.search(22))

# Remoção de uma chave
hash_table.delete(22)
print("Após remover a chave 22:")
hash_table.display()
'''

