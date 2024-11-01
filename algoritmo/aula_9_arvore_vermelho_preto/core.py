import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

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

def inserir2(lista, valor):
    
    if (valor < lista[0]):
        lista.insert(0, valor)
        return lista
    
    b = len(lista) - 1
    if (valor > lista[b]):
        lista.append(valor)
        return lista
    
    m = b // 2

    if (valor == lista[m]):
        lista.insert(m, valor)
        return lista

    a = 0
    b = m
    while(b >= a):
        print(a,b)
        zao = len(lista[a:b]) // 2
        if (valor < lista[zao]):
            b = m
        else:
            a = m
        #print(lista[a:b])

    return lista

vet = [0, 1, 3, 3, 4, 5, 6, 6, 7, 7, 10]
ret = inserir2(vet, 2)
print(ret)
