Significa que o aprendizado profundo se dá por muitas camadas de redes neurais. São bons para processar dados não estruturados como fotos, audios e vídeos em grande volume.

arquivo perceptron.py. O ajuste do sistema é empírico. É necessário modificar manualmente e observar os resultados.
É necessário separar os dados em treinamento e teste, geralmente 70% e 30% e verificar a acurácia.


O perceptron tem respostas lineares, ou seja, sim ou não. Isto é classificação, é ou não é um gato.

Modelos:
	Keras

[[Funções de ativação]] proporciona solução para problemas não lineares.

### Exemplos
#### 1 - Lógica XOR
A lógica XOR (OU Exclusivo) é uma operação binária que resulta em Verdadeiro (1) se, e somente se, as entradas forem diferentes; se as entradas forem iguais (ambas 0 ou ambas 1), a saída é Falso (0), funcionando como um comparador de diferença.

Deep_S01a_MLP1_XOR_ipynb.ipynb
Consiste em passar vários parâmetros X (várias colunas) e obter como resposta um deterniado valor. A função ativação vai determinar se é 0 ou 1, ou um falor flutuante sigmodal.

#### 2 - Rede Convolucional
Semana_03_Deep_CNN_Generica_MNIST.ipynb
Usa dataset mnist para definir se uma imagem é um determinado número. Retorna a probabilidade em ser entre 0..9

### 3 - Resnet50
Semana 04 - Deep_CNN_Resnet50.ipynb
É um modelo pretreinado de imagens que ajuda a classificar.


Qual modelo devo usar para um determinado propósito?