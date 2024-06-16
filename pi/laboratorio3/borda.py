def is_edge(image, x, y):
    """Verifica se um pixel é uma borda em uma imagem binária."""
    height, width = len(image), len(image[0])
    
    # Coordenadas dos pixels vizinhos (8-vizinhança)
    neighbors = [
        (-1, -1), (0, -1), (1, -1),
        (-1,  0),         (1,  0),
        (-1,  1), (0,  1), (1,  1)
    ]
    
    # Verifica se o pixel está na borda
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            if image[ny][nx] == 0 and image[y][x] == 1:
                return True
    
    return False

# Exemplo de uso
image = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

for linha in range(0, image.__len__()):
    for coluna in range(0, image.__len__()):
        if (is_edge(image, linha, coluna)):
            print('pixel', linha, coluna)
