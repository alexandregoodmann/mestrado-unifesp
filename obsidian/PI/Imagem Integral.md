## Atividade 1

Implementação de Imagem integral

~~Escreva um programa em C++ ou Python, utilizando a biblioteca do openCV. Ele deve~~
~~receber como entrada um arquivo contendo uma imagem e também as coordenadas x0,y0 e xn, yn de um retângulo totalmente contido na imagem. As coordenadas são números inteiros.~~

~~O programa deve abrir a imagem no modo monocromático (tons de cinza), mesmo que ela~~
~~seja colorida e exibí-la. Depois, ele deve calcular a [[Imagem Integral]] dessa imagem em tons de cinza. A partir da imagem integral e das coordenadas de entrada, o programa deve calcular a área do retângulo e a média da intensidade dentro do triângulo dado, imprimindo o resultado.~~

~~Por fim, o programa deve criar uma imagem colorida com uma cópia do conteúdo da~~
~~imagem em tons de cinza (conversão de imagem em tons de cinza para colorida), pintar os lados do retângulo sobre a imagem (escolha a cor) e exigir a imagem com o retângulo sobreposto.~~

Obs.: As coordenadas x0, y0 são sempre menores que as coordenadas xn e yn. Além disso, o retângulo deve ser criado de incluindo as coordenadas x0, y0 a xn, yn (por exemplo, se as
coordenadas forem 0,0 a 30,30, o retângulo inclui as coordenadas de origem e término).

Referencias da atividade
http://www.lps.usp.br/hae/apostila/integral.pdf
https://imaginebits.wordpress.com/2011/08/17/integral-image/

______________________________

A imagem integral é uma representação intermediária de uma imagem que é comumente usada em algoritmos de processamento de imagem para cálculos eficientes de características locais, como soma de pixels em uma região retangular.

A ideia fundamental por trás da imagem integral é que, em vez de calcular a soma de pixels repetidamente para diferentes regiões retangulares na imagem original, podemos pré-calcular uma representação acumulativa da imagem que nos permite calcular rapidamente a soma de pixels em qualquer região retangular.

A imagem integral é calculada de forma recursiva, onde cada valor na imagem integral é a soma de todos os pixels acima e à esquerda do pixel correspondente na imagem original. Esse processo pode ser representado pela seguinte equação:

\[ S(x, y) = I(x, y) + S(x-1, y) + S(x, y-1) - S(x-1, y-1) \]

Onde:
- \( S(x, y) \) é o valor na posição (x, y) na imagem integral.
- \( I(x, y) \) é o valor na posição (x, y) na imagem original.

O cálculo eficiente da imagem integral permite que operações como a soma de pixels em uma região retangular sejam realizadas em tempo constante, independentemente do tamanho da região, tornando-as extremamente úteis em algoritmos de detecção de características, detecção de objetos e muitas outras aplicações de visão computacional.

Uma vez calculada a imagem integral, podemos usar a seguinte fórmula para calcular a soma de pixels em uma região retangular definida pelas coordenadas (x1, y1) e (x2, y2):

\[ \text{Soma} = S(x2, y2) - S(x1-1, y2) - S(x2, y1-1) + S(x1-1, y1-1) \]

Essa fórmula nos permite realizar cálculos eficientes de características locais, como filtros de média ou detecção de bordas em uma região retangular específica da imagem.

------------------

## Meu codigo em python para calcular imagem integral

```python
import cv2
import numpy as np
import io
import os
from matplotlib import pyplot as plt

# limpar console
os.system('cls' if os.name == 'nt' else 'clear')

# Carregar a imagem em tons de cinza
img = cv2.imread('/home/alexandre/projetos/mestrado-unifesp/pi/laboratorio1/Lenna.png', cv2.IMREAD_GRAYSCALE)

#imagem para teste
#img = np.matrix([[5, 8, 1, 2, 9], [10, 8 ,7, 6, 2], [4, 3, 1, 4, 5], [8, 9, 2, 3, 5], [6, 8, 7, 1, 3]])

M, N = img.shape # linhas, colunas
I = np.zeros((M+1, N+1))
i = I
i[1:, 1:] = img

print('Imagem com primeira linha e colula zeradas\n', i)

for x in range(1, M+1):
	for y in range(1, N+1):
	I[x,y] = i[x,y] + I[x, y-1] + I[x-1, y] - I[x-1, y-1]

print('Imagem integral\n', I)
```


_________________

## Calculo de area com base na Imagem Integral 

Para calcular a área de um retângulo com base na imagem integral, você pode usar a seguinte fórmula:

Area = S(x2, y2) - S(x1-1, y2) - S(x2, y1-1) + S(x1-1, y1-1)

Onde:


- \( S(x, y) \) é o valor na posição (x, y) na imagem integral.
- \( (x1, y1) \) são as coordenadas do canto superior esquerdo do retângulo.
- \( (x2, y2) \) são as coordenadas do canto inferior direito do retângulo.

Esta fórmula calcula a soma de todos os pixels dentro do retângulo definido pelas coordenadas (x1, y1) e (x2, y2) usando os valores armazenados na imagem integral. 

Aqui está um exemplo de como você pode implementar isso em Python:

```python
def calcular_area_retangulo(imagem_integral, x1, y1, x2, y2):
    # Calcular a área usando a imagem integral
    area = imagem_integral[y2, x2] - imagem_integral[y1-1, x2] - \
           imagem_integral[y2, x1-1] + imagem_integral[y1-1, x1-1]
    return area

# Exemplo de uso:
# Suponha que você já tenha a imagem integral e as coordenadas do retângulo
imagem_integral = ...  # Sua imagem integral
x1, y1 = ...  # Coordenadas do canto superior esquerdo do retângulo
x2, y2 = ...  # Coordenadas do canto inferior direito do retângulo

# Calcular a área do retângulo
area_retangulo = calcular_area_retangulo(imagem_integral, x1, y1, x2, y2)
print("Área do retângulo:", area_retangulo)
```

Certifique-se de que as coordenadas do retângulo estão dentro dos limites da imagem e que a imagem integral foi calculada corretamente antes de usar essa função.

_____________________________
## Para calcular a média da intensidade

dos pixels dentro de um retângulo usando a imagem integral, você pode seguir uma abordagem semelhante à que usamos para calcular a área. A diferença é que, em vez de calcular a soma dos valores dos pixels, você calcula a soma das intensidades e, em seguida, divide pelo número total de pixels no retângulo.

Aqui está a fórmula para calcular a média da intensidade:

\[ \text{Média} = \frac{{S(x2, y2) - S(x1-1, y2) - S(x2, y1-1) + S(x1-1, y1-1)}}{{(x2 - x1 + 1) \times (y2 - y1 + 1)}} \]

Onde:
- \( S(x, y) \) é o valor na posição (x, y) na imagem integral.
- \( (x1, y1) \) são as coordenadas do canto superior esquerdo do retângulo.
- \( (x2, y2) \) são as coordenadas do canto inferior direito do retângulo.

Essa fórmula calcula a soma das intensidades de todos os pixels dentro do retângulo e, em seguida, divide pelo número total de pixels no retângulo para obter a média da intensidade.

Aqui está um exemplo de como você pode implementar isso em Python:

```python
def calcular_media_intensidade(imagem_integral, x1, y1, x2, y2):
    # Calcular a soma das intensidades usando a imagem integral
    soma_intensidades = imagem_integral[y2, x2] - imagem_integral[y1-1, x2] - \
                        imagem_integral[y2, x1-1] + imagem_integral[y1-1, x1-1]
    # Calcular o número total de pixels no retângulo
    num_pixels = (x2 - x1 + 1) * (y2 - y1 + 1)
    # Calcular a média da intensidade
    media_intensidade = soma_intensidades / num_pixels
    return media_intensidade

# Exemplo de uso:
# Suponha que você já tenha a imagem integral e as coordenadas do retângulo
imagem_integral = ...  # Sua imagem integral
x1, y1 = ...  # Coordenadas do canto superior esquerdo do retângulo
x2, y2 = ...  # Coordenadas do canto inferior direito do retângulo

# Calcular a média da intensidade dentro do retângulo
media_intensidade = calcular_media_intensidade(imagem_integral, x1, y1, x2, y2)
print("Média da intensidade:", media_intensidade)
```

Certifique-se de que as coordenadas do retângulo estão dentro dos limites da imagem e que a imagem integral foi calculada corretamente antes de usar essa função.

___________________

## Laboratório 02

~~Implementação de Transformação Afim~~

~~Escreva um programa em C++ ou Python, utilizando a biblioteca do openCV. Ele deve~~
~~receber como entrada um arquivo contendo uma imagem e também um arquivo contendo uma matriz de transformada afim, conforme dado nos exemplos.~~
~~O programa deve abrir a imagem e exibí-la. Depois deve ler o conteúdo da matriz afim,~~
~~exibir seu conteúdo e deve calcular a transformada afim dessa imagem.~~
~~Por fim, o programa deve exibir a imagem transformada.~~
~~Obs.:~~
1. ~~Vocês devem implementar a transformada inversa (veja as notas de aula).~~
2. ~~Para cada transformação afim, apenas uma matriz de transformação deve ser aplicada,~~
~~contendo a combinação correspondente das transformações solicitadas.~~
3. ~~O tamanho da imagem final deve ser igual ao da imagem original. (veja o código dado)~~
4. ~~As imagens de entrada e transformada devem ter o mesmo ponto de origem em 0,0. Isso quer dizer que após uma translação maior ou igual a um pixel, a imagem transformada deve~~
~~apresentar o conteúdo da imagem original deslocado.~~
~~Se for entregar o projeto em C++, envie em um pacote compactado de arquivos (.zip, .rar, ou~~
~~.tar.gz) os seguintes arquivos: a sua implementação (.cpp) e os arquivos de teste (.txt) contendo~~
~~transformações.~~
~~Se a entrega for em python, envie o notebook com todas as implementações e~~
~~transformações.~~
~~As seguintes transformações devem ser implementadas e enviadas:~~
~~a. um exemplo de rotação em torno do centro da imagem, seguida de redução de escala;~~
~~b. um exemplo de cizalhamento seguido de translação, seguido de rotação;~~
~~c. um exemplo rotação em torno do centro da imagem, seguida de aumento de escala.~~
~~Os parâmetros de cada transformação podem ser escolhidos por vocês, desde que haja uma~~
~~parte da imagem final ainda visível dentro do campo visual da imagem final.~~