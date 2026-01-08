
### Função degrau
Não utilizada em funções modernas
$y = 0$, se $x < limite$
$y = 1$, se $x >= limite$

### Função Sigmoidal
Utilizada em camadas ocultas de redes neurais; saída centralizada em zero ajuda a acelerar o treinamento. Retorna valores entre 0 e 1
$$
	y = \frac{1}{(1+e^{-x})}
$$
### Trangenta Hiperbólida
Retorna entre -1 e 1, acelera o treinamento. Sua saída centralizada em zero ajuda o treinamento.
 $$
 y = \frac{e^x - e^{-x}}{e^x + e^{-x}}
$$
### ReLu - Rectified Linear Unit
Torna o valor 0 se for menor que zero e mantém o valor se for maior que zero. Redes neurais convolucionais.
$$
y = max(0, x)
$$
## Funão Linear
Passa o valor de entrada diretamente para saída, ou seja, um número real. Não há transição de valor. Aplicado em caso onde precisa prever o valor de um imóvel considerando tamanho de quarto, localização m2. Utilizada em problemas de regressão.
$$
y = x
$$

### SoftMax
Problemas de classificação multiclasses. Poderá haver várias soluções de saídas, não somente true ou false, mas gato, cachorro, papagario.

$$
\frac{e^{z_i}}{\sum_{j=1}^{K}e^{z_j}}
$$
$e^{z_i}$ é o valor do elemento $i$ no vetor de entrada
$\sum_{j=1}^{K}e^{z_j}$ a soma dos elementos do vetor de entrada

![[Pasted image 20260107151954.png]]

| Função de Ativação      | Fórmula                 | Intervalo de Saída | Onde Usar na Prática                                                     | Vantagens                            | Desvantagens                   |
| ----------------------- | ----------------------- | ------------------ | ------------------------------------------------------------------------ | ------------------------------------ | ------------------------------ |
| **Linear (Identity)**   | f(x)=x                  | (-∞, +∞)           | Camada de saída em **regressão** (preço, temperatura, controle contínuo) | Simples, não distorce valores        | Não modela não-linearidade     |
| **Sigmoid (Logística)** | 1 / (1+e⁻ˣ)             | (0, 1)             | Saída de **classificação binária**, probabilidade                        | Interpretação probabilística         | Vanishing gradient, lenta      |
| **Tanh**                | (eˣ − e⁻ˣ)/(eˣ + e⁻ˣ)   | (-1, 1)            | RNNs antigas, dados centrados                                            | Zero-centered                        | Ainda sofre vanishing gradient |
| **ReLU**                | max(0, x)               | [0, +∞)            | **Padrão em CNNs e MLPs**                                                | Simples, rápida, eficiente           | Neurônios mortos               |
| **Leaky ReLU**          | max(αx, x)              | (-∞, +∞)           | CNNs profundas                                                           | Reduz neurônios mortos               | α fixo                         |
| **PReLU**               | max(αx, x), α treinável | (-∞, +∞)           | Visão computacional avançada                                             | Aprende o melhor α                   | Mais parâmetros                |
| **ELU**                 | x se x>0, α(eˣ−1)       | (-α, +∞)           | Redes profundas estáveis                                                 | Convergência melhor                  | Mais custo computacional       |
| **SELU**                | Escalada do ELU         | (-∞, +∞)           | Redes auto-normalizáveis                                                 | Normalização automática              | Requer arquitetura específica  |
| **GELU**                | x·Φ(x)                  | (-∞, +∞)           | **Transformers (BERT, GPT)**                                             | Muito eficaz em NLP                  | Mais complexa                  |
| **Swish**               | x·sigmoid(x)            | (-∞, +∞)           | CNNs modernas (EfficientNet)                                             | Melhor que ReLU em muitos casos      | Mais lenta                     |
| **Mish**                | x·tanh(ln(1+eˣ))        | (-∞, +∞)           | Visão computacional experimental                                         | Suave, bons resultados               | Alto custo computacional       |
| **Softmax**             | eˣᵢ / Σeˣ               | (0,1), soma=1      | Saída de **classificação multiclasse**                                   | Interpretação probabilística         | Sensível a outliers            |
| **Hard Sigmoid**        | Aproximação linear      | (0,1)              | Mobile / Edge AI                                                         | Rápida                               | Menos precisa                  |
| **Hard Swish**          | Aproximação do Swish    | (-∞, +∞)           | Redes embarcadas (MobileNetV3)                                           | Boa performance em hardware limitado | Aproximação                    |
| **Softplus**            | ln(1+eˣ)                | (0, +∞)            | Alternativa suave ao ReLU                                                | Sempre diferenciável                 | Mais lenta                     |
| **Softsign**            | x/(1+                   | x                  | )                                                                        | (-1,1)                               | Casos específicos              |
| **Threshold (Step)**    | 0 ou 1                  | {0,1}              | **Perceptron clássico**                                                  | Simples                              | Não diferenciável              |