def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        # Verifica se o elemento está no meio
        if lista[meio] == elemento:
            return meio  # Retorna o índice do elemento
        
        # Se o elemento é maior, ignora a metade esquerda
        elif lista[meio] < elemento:
            inicio = meio + 1
            
        # Se o elemento é menor, ignora a metade direita
        else:
            fim = meio - 1
    
    return -1  # Retorna -1 se o elemento não foi encontrado
