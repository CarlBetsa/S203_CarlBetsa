class Pessoa(object):
    nome = None
    idade = None

    def __init__(self, nome, idade):
        self.nome = nome
        self.dade = idade

    def envelhecer(self):
        self.idade += 1

class Atleta(Pessoa):
    peso = None
    aposentado = None

    def __init__(self, nome, idade, peso):
        super().__init__(nome, idade)
        self.peso = peso

    def aquecer(self):
        print("Atleta aquecido")

    def aposentar(self):
        self.aposentado = True

class Corredor(Atleta):
    def correr(self):
        print('Corredor correndo...')

class Nadador(Atleta):
    def nadar(self):
        print('Nadador nadando...')

class Ciclista(Atleta):
    def pedalar(self):
        print('Ciclista pedalando...')

corredor = Corredor('Vanderlei', 27, 75)
corredor.aquecer()
corredor.correr()

nadador = Nadador('Gustavo', 35, 80)
print('Está aposentado? ')
if nadador.aposentado:
    print('Sim')
else:
    print('Não')

nadador.nadar()
nadador.envelhecer()
nadador.aposentar()

print('Agora já está aposentado? ')
print('Sim' if nadador.aposentado else 'Nâo')