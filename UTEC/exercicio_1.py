def exercicio_1():
    print('1) Haz un programa que pida dos números e imprima el más grande.')
    primeiro = int(input("Digite o primeiro número: "))
    segundo = int(input("Digite o segundo número: "))
    vet = [primeiro, segundo]
    maior = max(vet)
    print(f"O maior número é: {maior}")

def exercicio_2():
    print('2) Hacer un programa que pida un valor y muestre en pantalla si el valor es positivo o negativo.')
    numero = int(input("Digite algum número: "))
    if (numero > 0):
        print('Positivo')
    else:
        print('Negativo')

def exercicio_3():
    print('3) Escriba un programa que verifique si una letra escrita es "F" o "M". Como la letra, escriba: F - Femenino, M - Masculino.')
    letra = input("Digite F ou M: ")
    if (letra.upper() == 'F'):
        print('F = Feminino')
    elif (letra.upper() == 'M'):
        print('M = Masculino')
    else:
        print('Opção inválida')

def exercicio_4():
    print('4) Escriba un programa que verifique si una letra escrita es una vocal o una consonante.')
    vogais = 'aeiou'
    letra = input("Digite uma letra: ")   
    if (letra.__len__() > 1):
        print('Opção inválida')
    elif (letra.lower() in vogais):
        print('Vogal')
    else: 
        print('Consoante')

def exercicio_5():
    print('5) Haga un programa para leer dos notas parciales de un alumno. El programa debe calcular el promedio alcanzado por el estudiante y presentar:')
    primeiro = int(input("Digite o primeiro número: "))
    segundo = int(input("Digite o segundo número: "))
    vet = [primeiro, segundo]
    media = (primeiro+segundo)/2

    if media == 10:
        print('El mensaje "Aprobado con 10", si la media es igual a diez.')
    elif media >= 7:
        print('El mensaje "Aprobado", si el promedio alcanzado es mayor o igual a siete;')
    else:   
        print('El mensaje "No Aprobado", si el promedio es menor a siete;')
    
exercicio_5()