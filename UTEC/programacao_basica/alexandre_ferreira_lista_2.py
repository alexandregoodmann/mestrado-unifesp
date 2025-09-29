'''
Conecte OO ao contexto da especialização em Robótica e IA.
R4 — Hierarquia de Robôs : Robo base (x, y, bateria); RoboTerrestre vs RoboAereo com mover() polimórfico.
R5 — Projeto Integrador : Ambiente que gerencia múltiplos robôs (composição), tarefas de exploração/coleta, relatório de energia.
'''
# --------------------------------------------------------------------------------
# R1 — Sensor : classe Sensor (tipo, valor); método ler() com valor simulado.
# --------------------------------------------------------------------------------
class Sensor:
    sensores = {}
    def __init__(self, tipo, valor):
        self.valor = valor
        self.tipo = tipo
        self.sensores.update({tipo: valor})

    def ler(self, tipo):
        return self.sensores.get(tipo)
    
    def listaSensores(self):
        return self.sensores
    
sensor1 = Sensor('distancia', 3.31)
sensor2 = Sensor('temperatura', 45)
sensor3 = Sensor('presenca', True)

# possível ler toda a lista apartir de um objeto
lista = sensor1.listaSensores()
print('Lista de Sensores: ', lista)

# da mesma forma, possível ler um sentor a partir de qualquer objeto
valor = sensor1.ler('temperatura')
print('Valor de Temperatura: ', valor)

# --------------------------------------------------------------------------------
# R2 — Atuador : classe Atuador (estado); métodos ligar() / desligar() .
# --------------------------------------------------------------------------------
class Atuador:
    __ligado = False
    def __init__(self):
        pass

    def ligar(self):
        self.__ligado = True

    def desligar(self):
        self.__ligado = False

    def getStatus(self):
        return self.__ligado
    
atuador = Atuador()
print('Status ao criar: ', atuador.getStatus())
atuador.ligar()
print('Status ao ligar : ', atuador.getStatus())
atuador.desligar()
print('Status ao desligar: ', atuador.getStatus())

# --------------------------------------------------------------------------------
# R3 — Motor : atributo privado _velocidade e @property para controles; simular aceleração/frenagem.
# --------------------------------------------------------------------------------
class Motor:
    _velocidade = 0
    def __init__(self):
        pass

    @property
    def velocidade(self):
        return self._velocidade

    @velocidade.setter
    def velocidade(self, valor):
        self._velocidade += valor

    def freiar(self, forca):
        self._velocidade -= forca

motor = Motor()
for i in range(0, 100):
    motor.velocidade = i
    print('acelerando: ', motor.velocidade)

while motor.velocidade > 0:
    motor.freiar(10)
    print('freiando: ', motor.velocidade)
