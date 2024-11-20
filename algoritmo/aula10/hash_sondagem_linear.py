class HashSondagemLinear:
    def __init__(self, size):
        # Inicializa a tabela hash com None para cada posição
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        # Função hash da divisão
        return key % self.size
    
    def insert(self, key, value):
        # Calcula o índice usando a função hash
        index = self.hash_function(key)
        
        # Sondagem linear para resolver colisões
        initial_index = index
        while self.table[index] is not None:
            # Se a chave já existir, atualiza o valor
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            # Move para a próxima posição
            index = (index + 1) % self.size
            # Checa se voltamos ao índice inicial (tabela cheia)
            if index == initial_index:
                print("Erro: A tabela hash está cheia.")
                return
        
        # Insere o par chave-valor na posição encontrada
        self.table[index] = (key, value)
    
    def search(self, key):
        # Calcula o índice usando a função hash
        index = self.hash_function(key)
        
        # Sondagem linear para encontrar a chave
        initial_index = index
        while self.table[index] is not None:
            # Verifica se a chave está presente
            if self.table[index][0] == key:
                return self.table[index][1]
            # Move para a próxima posição
            index = (index + 1) % self.size
            # Checa se voltamos ao índice inicial (chave não encontrada)
            if index == initial_index:
                break
        return None  # Retorna None se a chave não for encontrada
    
    def delete(self, key):
        # Calcula o índice usando a função hash
        index = self.hash_function(key)
        
        # Sondagem linear para encontrar e remover a chave
        initial_index = index
        while self.table[index] is not None:
            # Se a chave é encontrada, remove-a (define a posição como None)
            if self.table[index][0] == key:
                self.table[index] = None
                return True
            # Move para a próxima posição
            index = (index + 1) % self.size
            # Checa se voltamos ao índice inicial
            if index == initial_index:
                break
        return False  # Retorna False se a chave não for encontrada
    
    def display(self):
        # Exibe o conteúdo da tabela hash
        for i, item in enumerate(self.table):
            print(f"Índice {i}: {item}")
'''

# Exemplo de uso
hash_table = HashSondagemLinear(11)  # Cria uma tabela hash com 11 posições

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

