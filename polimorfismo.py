"""Polimorfismo é um conceito da programação orientada a objetos que se refere à habilidade de objetos de 
diferentes classes responderem ao mesmo método de maneira diferente. O polimorfismo permite que diferentes 
objetos de classes relacionadas possam ser tratados de maneira uniforme, aumentando a flexibilidade e a 
modularidade do código. Em Python, o polimorfismo pode ser implementado por meio de herança e sobrescrita de métodos. 
Quando uma classe derivada herda um método de sua classe base, ela pode sobrescrevê-lo com uma implementação 
específica que atenda às suas necessidades."""

# de maneira simples, o objetivo é criar um único nome de método para que eu possa usar em diferentes objetos com comportamentos diferentes, evitando a repetição.


class Veiculo():
    
    def __init__(self, marca, modelo):
        print("Veículo criado com sucesso!")
        print("\n")
        self.marca = marca
        self.modelo = modelo

    # propositalmente não iremos colocar nada em acelerar ou frear, pois na teoria do codigo cada veículo tem seu próprio comportamento.

    def acelerar(self):
        pass
        
    def frear(self):
        pass

class Carro(Veiculo):

    def acelerar(self):
        print("O carro está acelerando")

    def frear(self):
        print("O carro está freando")

class Moto(Veiculo):

    def acelerar(self):
        print("A moto está acelerando")

    def frear(self):
        print("A moto está freando")


# Repare que moto e carro não possuem método construtor, mas mesmo assim conseguimos criar objetos deles, isso acontece porque a classe veiculo possui um método construtor, e como carro e moto herdam de veiculo, eles também herdam o método construtor.

class Jato(Veiculo):

    def acelerar(self):
        print("O jato está acelerando")

    def frear(self):
        print("O jato está freando")

    def decolar(self): # esse método só existe em jato, e não em carro ou moto nem veículo
        print("O jato está decolando")
    
    def misseis(self): # esse também só existe em jato
        print("O jato está lançando misseis")


# usando os métodos de lista, podemos criar uma lista de veículos e percorrer a lista e usar os métodos de cada um deles, sem precisar saber qual é o tipo de veículo, pois todos eles tem o método acelerar e frear, e o polimorfismo faz com que cada um deles tenha seu próprio comportamento.

veiculos = [Carro("Fiat", "Uno"), Moto("Honda", "CG"), Jato("Boeing", "747")]

# porém, se eu quiser usar o método decolar ou misseis, eu preciso saber se o veículo é um jato, pois só jato tem esses métodos, e para isso eu preciso fazer um if, pois não posso simplesmente chamar o método decolar ou misseis, pois se o veículo não for um jato, ele não vai ter esses métodos.

for veiculo in veiculos:

    # para cada veículo na lista de veículos
    veiculo.acelerar()
    veiculo.frear()
    print("\n")

    # se o veículo for uma instância de jato
    if isinstance(veiculo, Jato): 
        veiculo.decolar()
        veiculo.misseis()
        print("\n")

# Mas é valido dizer que não temos apenas uma instância do método acelerar e frear, pois cada veículo tem seu próprio método acelerar e frear, e isso é o polimorfismo, pois cada veículo tem seu próprio comportamento, mas todos eles tem o mesmo nome de método, e isso é o polimorfismo.