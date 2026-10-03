class Perceptron:
  def __init__(self):
    # Inicialização das matrizes de pesos e vetores de bias para uma rede neural com a arquitetura:
    # 784 entradas -> 256 neurônios na camada oculta 1 -> 128 neurônios na camada oculta 2 ->
    # 64 neurônios na camada oculta 3 -> 64 neurônios na camada oculta 4 -> 10 neurônios na camada de saída.
    # W1, b1 (784 entradas -> 256 neurônios)
    self.W1 = 2 * np.random.rand(256, 784) - 1
    self.b1 = 2 * np.random.rand(256, 1) - 1

    # W2, b2 (256 neurônios -> 128 neurônios)
    self.W2 = 2 * np.random.rand(128, 256) - 1
    self.b2 = 2 * np.random.rand(128, 1) - 1

    # W3, b3 (128 neurônios -> 64 neurônios)
    self.W3 = 2 * np.random.rand(64, 128) - 1
    self.b3 = 2 * np.random.rand(64, 1) - 1

    # W4, b4 (64 neurônios -> 64 neurônios)
    self.W4 = 2 * np.random.rand(64, 64) - 1
    self.b4 = 2 * np.random.rand(64, 1) - 1

    # W5, b5 (64 neurônios -> 10 neurônios)
    self.W5 = 2 * np.random.rand(10, 64) - 1
    self.b5 = 2 * np.random.rand(10, 1) - 1

  def forward(self, x):
    # Camada 1 (784 -> 256)
    self.s1 = np.dot(self.W1, x) + self.b1
    self.z1 = sigmoid(self.s1)

    # Camada 2 (256 -> 128)
    self.s2 = np.dot(self.W2, self.z1) + self.b2
    self.z2 = sigmoid(self.s2)

    # Camada 3 (128 -> 64)
    self.s3 = np.dot(self.W3, self.z2) + self.b3
    self.z3 = sigmoid(self.s3)

    # Camada 4 (64 -> 64)
    self.s4 = np.dot(self.W4, self.z3) + self.b4
    self.z4 = sigmoid(self.s4)

    # Camada de Saída (64 -> 10)
    self.s5 = np.dot(self.W5, self.z4) + self.b5
    self.z5 = softmax(self.s5)

    return self.z5

  def backprop(self, x, y_des):
    # Chama o passo forward para obter as ativações
    self.y = self.forward(x)

    # Delta para a camada de saída (softmax + entropia cruzada)
    self.d5 = self.y - y_des

    # Deltas para as camadas ocultas
    self.d4 = np.dot(self.W5.T, self.d5) * (self.z4 - self.z4**2)
    self.d3 = np.dot(self.W4.T, self.d4) * (self.z3 - self.z3**2)
    self.d2 = np.dot(self.W3.T, self.d3) * (self.z2 - self.z2**2)
    self.d1 = np.dot(self.W2.T, self.d2) * (self.z1 - self.z1**2)

    # Gradientes para os pesos
    self.dW5 = np.dot(self.d5, self.z4.T)
    self.dW4 = np.dot(self.d4, self.z3.T)
    self.dW3 = np.dot(self.d3, self.z2.T)
    self.dW2 = np.dot(self.d2, self.z1.T)
    self.dW1 = np.dot(self.d1, x.T)

    # Gradientes para os biases
    self.db5 = self.d5
    self.db4 = self.d4
    self.db3 = self.d3
    self.db2 = self.d2
    self.db1 = self.d1

    # Taxa de aprendizado
    eta = 0.1

    # Atualiza pesos e biases
    self.W1 -= eta * self.dW1
    self.b1 -= eta * self.db1
    self.W2 -= eta * self.dW2
    self.b2 -= eta * self.db2
    self.W3 -= eta * self.dW3
    self.b3 -= eta * self.db3
    self.W4 -= eta * self.dW4
    self.b4 -= eta * self.db4
    self.W5 -= eta * self.dW5
    self.b5 -= eta * self.db5

    # Calcula o custo de entropia cruzada (adicionando um pequeno epsilon para evitar log(0))
    self.ce = -np.sum(y_des * np.log(self.y + 1e-9))

    return self.ce