def calcular_imagem_integral(imagem):
    altura, largura = imagem.shape
    integral = [[0 for _ in range(largura)] for _ in range(altura)]

    # Primeira linha e primeira coluna
    integral[0][0] = imagem[0][0]

    # Preenche a primeira linha
    for j in range(1, largura):
        integral[0][j] = integral[0][j - 1] + imagem[0][j]

    # Preenche a primeira coluna
    for i in range(1, altura):
        integral[i][0] = integral[i - 1][0] + imagem[i][0]

    # Preenche o restante da imagem integral
    for i in range(1, altura):
        for j in range(1, largura):
            integral[i][j] = (imagem[i][j] + integral[i - 1][j] +
                              integral[i][j - 1] - integral[i - 1][j - 1])

    return integral

# Exemplo de uso
imagem = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

integral = calcular_imagem_integral(imagem)
for linha in integral:
    print(linha)
