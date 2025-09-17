# --------------------------------------------------------------------------------------
# UTEC - Especialização em Robótica e Inteligência Artificial
# Disciplina: Programação Básica
# Aluno: Alexandre Ferreira e Silva
# Atividade 01
# Cada método é um exercício. Simplesmente chame um método no final do arquivo
# --------------------------------------------------------------------------------------
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
    
def exercicio_6():
    print('6) Haz un programa que lea tres números y muestre el más grande.')
    entrada = []
    for i in range(0,3):
        numero = int(input("Digite um número: "))
        entrada.append(numero)
    maior = max(entrada)
    print(f"O maior número é: {maior}")

def exercicio_7():
    print('7) Haz un programa que lea tres números y muestre el mayor y el menor de ellos.')
    entrada = []
    for i in range(0,3):
        numero = int(input("Digite um número: "))
        entrada.append(numero)
    maior = max(entrada)
    menor = min(entrada)
    print(f"O maior número é: {maior} e o menor é: {menor}")

def exercicio_8():
    print('8) Haz un programa que pregunte el precio de tres productos y te diga qué producto debes comprar, sabiendo que la decisión es siempre la más barata.')
    entrada = []
    for i in range(0,3):
        numero = int(input("Digite o valor do produto: "))
        entrada.append(numero)
    menor = min(entrada)
    print(f"O produto mais barato é: {menor}")

def exercicio_9():
    print('    9) Escriba un programa que lea tres números y los muestre en orden descendente.')
    entrada = []
    for i in range(0,3):
        numero = int(input("Digite o número: "))
        entrada.append(numero)
    rever = sorted(entrada, reverse=True)
    print(f"O produto mais barato é: {rever}")

def exercicio_10():
    print('10) Haz un programa que te pregunte en qué turno estudias. Pida escribir M-Mañana o V-Tarde o N-Noche. Imprime el mensaje "Buen Dia!", "Buenas Tardes!" o “Buenas Noches!" o "¡Valor no válido!", según sea el caso.')
    entrada = input("Em que turno você trabalha? M-Mañana o V-Tarde o N-Noche:")
    if entrada.upper() == 'M':
        print('Bom dia')
    elif entrada.upper() == 'T':
        print('Boa tarde')
    elif entrada.upper() == 'N':   
        print('Boa noite')
    else:
        print('Entrada inválida')

def exercicio_11():
    print('11) Escriba un programa que declare un vector con 10 valores enteros predefinidos. El programa debe leer un valor entero e informar si el valor se encuentra en el vector y, de ser así, en qué posición(es) se encontró el valor. Al final, el programa debería ordenar el vector en orden descendente y escribir todos los valores en la pantalla.')
    vet = [3, 29, 6, 12, 1, 0, 82, 9, 63, 7]
    numero = int(input("Digite o número: "))
    index = vet.index(numero)
    rever = sorted(vet, reverse=True)
    print(f"O número encontra-se no índex {index}")
    print(f"Vetor Original: {vet}")
    print(f"Vetor invertido: {rever}")

def exercicio_12():
    print('12) Escriba un programa que lea 5 nombres (cadena) y 5 edades (enteros) y los almacene en 2 vectores. Luego, el programa deberá escribir el nombre de la persona mayor y el nombre de la persona más joven en la pantalla.')
    nomes = []
    idades = []
    for i in range(5):
        nomes.append(input(f"Nome {i+1}: "))
        idades.append(int(input("Idade: ")))

    print("Mais velho:", nomes[idades.index(max(idades))])
    print("Mais jovem:", nomes[idades.index(min(idades))])

def exercicio_13():
    print('13) Escribe un programa que calcule el IMC de una persona (IMC = masa en kg / altura en metros al cuadrado) e informe su clasificación según la tabla disponible en este enlace')

    peso = float(input("Informe seu peso (kg): "))
    altura = float(input("Informe sua altura (m): "))
    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 25:
        print("Classificação: Peso normal")
    elif imc < 30:
        print("Classificação: Sobrepeso")
    elif imc < 35:
        print("Classificação: Obesidade grau I")
    elif imc < 40:
        print("Classificação: Obesidade grau II")
    else:
        print("Classificação: Obesidade grau III (mórbida)")

def exercicio_14():
    print('14) Escriba un programa para determinar el número de dígitos en un entero positivo dado.')
    numero = int(input("Digite um número: "))
    print("Número de dígitos:", len(str(numero)))

exercicio_14()