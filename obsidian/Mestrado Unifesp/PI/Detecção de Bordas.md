Um algoritmo clássico para detecção de bordas em imagens é o operador Sobel. O operador Sobel é um filtro usado em processamento de imagem e visão computacional para encontrar a aproximação do gradiente da intensidade da imagem. Ele é usado para destacar as regiões de alta variação de intensidade que geralmente correspondem às bordas na imagem.

Aqui está um exemplo simples de como implementar o operador Sobel em Python usando a biblioteca OpenCV:

```python
import cv2
import numpy as np

def detect_edges(image):
    # Converte a imagem para tons de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplica o operador Sobel nos eixos x e y
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    
    # Calcula a magnitude do gradiente
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    
    # Normaliza a magnitude para o intervalo [0, 255]
    magnitude = np.uint8(magnitude)
    
    return magnitude

# Carrega a imagem
image = cv2.imread('imagem.jpg')

# Detecta as bordas na imagem
edges = detect_edges(image)

# Mostra a imagem original e a imagem com as bordas detectadas
cv2.imshow('Original', image)
cv2.imshow('Bordas', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

Este código aplica o operador Sobel nos eixos x e y da imagem para detectar as bordas e, em seguida, calcula a magnitude do gradiente. Finalmente, mostra a imagem original e a imagem com as bordas detectadas. Certifique-se de substituir `'imagem.jpg'` pelo caminho do arquivo da sua imagem.