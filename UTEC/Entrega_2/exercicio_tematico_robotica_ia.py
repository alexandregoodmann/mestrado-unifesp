# --------------------------------------------------------------------------------------
# UTEC - Especialização em Robótica e Inteligência Artificial
# Disciplina: Programação Básica
# Aluno: Alexandre Ferreira e Silva
# Atividade 02
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# Conecte OO ao contexto da especialização em Robótica e IA.
# --------------------------------------------------------------------------------

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

# --------------------------------------------------------------------------------
# R4 — Hierarquia de Robôs : Robo base (x, y, bateria); RoboTerrestre vs RoboAereo com mover() polimórfico.
# --------------------------------------------------------------------------------
class RoboBase:
    x = 0
    y = 0
    bateria = 100
    def __init__(self):
        pass

    def mover(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Robo Base x: {self.x}, y:{self.y}"

class RoboTerrestre(RoboBase):
    def __init__(self):
        pass
    def __str__(self):
        return f"Terrestre x: {self.x}, y:{self.y}"

class RoboAereo(RoboBase):
    z = 0
    def __init__(self):
        pass
    
    def mover(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Aereo x: {self.x}, y:{self.y}, z: {self.z}"

base = RoboBase()
base.mover(10, 20)
print(base)

terrestre = RoboTerrestre()
terrestre.mover(30, 40)
print(terrestre)

aereo = RoboAereo()
aereo.mover(50, 60, 70)
print(aereo)


# --------------------------------------------------------------------------------
# R5 — Projeto Integrador : Ambiente que gerencia múltiplos robôs (composição), tarefas de exploração/coleta, relatório de energia.
# --------------------------------------------------------------------------------
class RoboService:
    robos = []
    def __init__(self):
        pass
    def addRobo(self, robo):
        self.robos.append(robo)

    def explorar(self):
        for robo in self.robos:
            while robo.bateria > 0:
                robo.bateria -= 1
                print("Explorando...: ", robo, f" - zNivel Bateria: {robo.bateria}")

roboService = RoboService()
roboService.addRobo(base)
roboService.addRobo(terrestre)
roboService.addRobo(aereo)

roboService.explorar()
    