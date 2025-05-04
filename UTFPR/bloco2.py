entrada = [30, 10, 5, 50, 40, -1]
numeros = entrada[:5]
print(numeros)
qtd = len(numeros)
soma = 0

for num in numeros:
    if num == -1:
        break
    elif num >= 0:
        soma += num
    else:
        print("Apenas números positivos são permitidos!")

media = soma / qtd
maior = max(numeros)
menor = min(numeros)
maiores_que_media = sum(1 for n in numeros if n > media)

# Exibição dos resultados
print(f"Quantidade de números na lista: {qtd}")
print(f"Soma dos números da lista: {soma}")
print(f"Média dos valores da lista: {media:.2f}")
print(f"Maior número da lista: {maior}")
print(f"Menor número da lista: {menor}")
print(f"Quantidade de números maiores que a média: {maiores_que_media}")

print("A quantidade de números na lista: 5")
print("A soma dos números da lista: 133")
print("A média considerando os valores na lista: 26.6")
print("O maior número da lista: 60")
print("O menor número da lista: 8")
print("Quantos números da lista são maiores que a média: 2")