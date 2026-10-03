import numpy as np

class Perceptron:
    def __init__(self, n_inputs, learning_rate=0.1, n_epochs=100):
        # Inicializa pesos aleatórios (inclui o bias como último peso)
        self.weights = np.random.randn(n_inputs + 1) * 0.01
        self.learning_rate = learning_rate
        self.n_epochs = n_epochs

    def activation(self, x):
        # Função degrau
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        # Adiciona o bias (1) no final dos inputs
        inputs_with_bias = np.append(inputs, 1)
        weighted_sum = np.dot(inputs_with_bias, self.weights)
        return self.activation(weighted_sum)

    def fit(self, X, y):
        for epoch in range(self.n_epochs):
            for inputs, target in zip(X, y):
                prediction = self.predict(inputs)
                error = target - prediction
                # Atualização dos pesos
                inputs_with_bias = np.append(inputs, 1)
                self.weights += self.learning_rate * error * inputs_with_bias
                

    def lerArquivo(self):
        data = np.loadtxt('perceptron_dataset.csv', delimiter=',', skiprows=1)
        X = data[:, :2]
        y = data[:, 2]
        return X, y
    
    
    def accuracy(self, X, y):
        correct = 0
        for inputs, target in zip(X, y):
            prediction = self.predict(inputs)
            if prediction == target:
                correct += 1
        accuracy = (correct / len(y)) * 100
        return accuracy
    
    def salvarPesos(self):
        np.save("weights.npy", perceptron.weights)
        
    def lerPesos(self):
        self.weights = np.load("weights.npy")
        

# ------------------------------
# Exemplo: Treinando perceptron para aprender a função lógica AND
# ------------------------------

'''
# Dados de entrada (x1, x2)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Saídas desejadas (AND)
y = np.array([0, 0, 0, 1])
'''

# Cria perceptron
perceptron = Perceptron(n_inputs=2, learning_rate=0.01, n_epochs=10)
X, y = perceptron.lerArquivo()
X = X /100

# Treina
#perceptron.fit(X, y)
#perceptron.salvarPesos()
perceptron.lerPesos()
# ==========================================
# TESTAR RESULTADOS
# ==========================================

print("\n=== RESULTADOS ===")

correct = 0

for inputs, target in zip(X, y):

    prediction = perceptron.predict(inputs)

    print(
        f"Entrada: {inputs} | "
        f"Esperado: {int(target)} | "
        f"Previsto: {prediction}"
    )

    if prediction == target:
        correct += 1

# ==========================================
# ÍNDICE DE ACERTOS
# ==========================================

accuracy = (correct / len(y)) * 100

print("\n========================")
print(f"Total de amostras: {len(y)}")
print(f"Acertos: {correct}")
print(f"Precisão: {accuracy:.2f}%")
print("========================")