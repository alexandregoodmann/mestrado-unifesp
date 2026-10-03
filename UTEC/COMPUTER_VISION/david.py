class Perceptron():
  def _init_(self):
    self.b1 = np.random.random((256, 1)) * 2 - 1
    self.b2 = np.random.random((64, 1)) * 2 - 1
    self.b3 = np.random.random((10, 1)) * 2 - 1
    self.W1 = np.random.random((256, 784)) * 2 - 1
    self.W2 = np.random.random((64, 256)) * 2 - 1
    self.W3 = np.random.random((10, 64)) * 2 - 1

  def forward(self,x):
    self.s1 = np.dot(self.W1,x) + self.b1
    self.z1 = sigmoid(self.s1)
    self.s2 = np.dot(self.W2,self.z1) + self.b2
    self.z2 = sigmoid(self.s2)
    self.s3 = np.dot(self.W3,self.z2) + self.b3
    self.z3 = softmax(self.s3)
    return self.z3

  def backprop(self, x ,y_des):
    self.y = self.forward(x)
    self.d3 = self.y - y_des
    self.d2 = np.dot(self.W3.transpose(), self.d3) * self.z2 * (1 - self.z2)
    self.d1 = np.dot(self.W2.transpose(), self.d2) * self.z1 * (1 - self.z1)
    self.db1 = self.d1
    self.db2 = self.d2
    self.db3 = self.d3
    self.dW1 = np.dot(self.d1, x.transpose())
    self.dW2 = np.dot(self.d2, self.z1.transpose())
    self.dW3 = np.dot(self.d3, self.z2.transpose())
    self.eta=0.1
    self.W1 -= self.eta * self.dW1
    self.W2 -= self.eta * self.dW2
    self.W3 -= self.eta * self.dW3
    self.b1 -= self.eta * self.db1
    self.b2 -= self.eta * self.db2
    self.b3 -= self.eta * self.db3
    self.ce = -np.sum(y_des * np.log(self.y))
    return self.ce