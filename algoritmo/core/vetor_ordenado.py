import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

def pesquisar_ordenada(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if lista[meio] == elemento:
            return meio  # Retorna o índice do elemento
        
        elif lista[meio] < elemento:
            inicio = meio + 1
            
        else:
            fim = meio - 1
    
    return -1

def inserir_ordenada(lista, valor):

    if len(lista) == 0:
        lista.append(valor)
        return
    
    if (valor < lista[0]):
        lista.insert(0, valor)
        return 
    
    a = 0
    b = len(lista) - 1
    if (valor > lista[b]):
        lista.append(valor)
        return 
    
    m = b // 2

    if (valor == lista[m]):
        lista.insert(m, valor)
        return 

    while(b - a > 1):
        if (valor == lista[m]):
            lista.insert(m, valor)
            return 
        if (valor < lista[m]):
            # esquerdo
            b = m
            m = b // 2
        else:
            #direito
            a = m
            m = (a + b) // 2
    lista.insert(b, valor)
'''
vet = [0, 1, 3, 3, 4, 5, 6, 6, 7, 7, 10, 13, 27, 33, 41, 45, 46, 50, 58, 59, 60]
ret = inserir(vet, 30)
print(ret)
'''