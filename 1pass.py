# Uma classe é como um construtor de objetos ou um "projeto" para criar objetos.
class carro:
# init é uma função que aplica para inicializar uma classe, aplicado automaticamente definindo o comportamento inicial de um objeto
    def __init__(self, marca, capacidade, placa):
# Com a palavra-chave self conseguimos acessar os atributos e métodos de uma classe em Python.
        self.marca = marca
# self está acessando os atributos de marca
        self.capacidade = capacidade
# self está acessando os atributos de capacidade
        self.placa = placa
# self está acessando os atributos de placa
        pass
# Você evita receber um erro quando código vazio não é permitido. código vazio não é permitido em loops, definições de função, definições de classe ou em instruções if.
    def ligar(self):
        print('Estou ligando')

    def desligar(self):
        print('Estou desligando')

    def values_carros(self):
        print(self.marca, self.capacidade, self.placa)

carro1 = carro('Audi', '\n5 pessoas', '\n562cV')

carro1.ligar()
carro1.desligar()
carro1.values_carros()