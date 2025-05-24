with open("limpar.txt") as file:
    for linha in file:
        linha = linha.replace('[', '')
        linha = linha.replace(']', '')
        linha = linha.replace('     ', ',')
        linha = linha.replace(' ', '')
        i = linha.index(',')
        var = linha[i+1:].split('\n')
        print(var[0])
