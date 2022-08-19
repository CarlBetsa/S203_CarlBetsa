class Pessoa(object):
    nome = None
    sexo = None
    idade = None

    def __init__(self, nome, sexo, idade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

class Cidadao(Pessoa):
    cpf = None

    def __init__(self, nome, sexo, idade, cpf):
        super().__init__(nome, sexo, idade)
        self.cpf = cpf

nome = input("Entre com o nome: ")
sexo = input("Entre com o sexo: ")
idade = input("Entre com o idade: ")
cpf = input("Entre com o cpf: ")

cidadao = Cidadao(nome, sexo, idade, cpf)

print(cidadao.nome)
