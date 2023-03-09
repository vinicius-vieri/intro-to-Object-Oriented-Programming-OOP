# na definiçao comum, herança é algo que se herda, ou seja, algo que é passado de pai para filho por exemplo.
# na programação orientada a objetos, herança é um conceito que permite que uma classe herde características e comportamentos de outra classe.
# uma superclasse é uma classe que é herdada por outras classes, ou seja, é a classe pai ou mãe.
# uma subclasse é uma classe que herda características e comportamentos de outra classe, ou seja, é a classe filha ou subclasse.
# é interessante ressaltar que uma subclasse pode ter um método com o mesmo nome de um método da superclasse, mas com comportamentos diferentes.

# criando uma classe mãe ou superclasse

class Animal():

    # criando um método construtor
    def __init__(self):
        print("Animal criado")

    
    def mostrar(self):
        print("Olá, eu sou um animal")

    
    def barulho(self):
        print("Eu não sei fazer barulho pois sou um animal genérico.")
        pass # pass é uma palavra reservada que indica que não há nada dentro do método. Porém por hora não iremos utilizar o método barulho da classe pai.


# criando duas subclasses ou classes filho, o porco e o galo.

class Porco(Animal):
    
        # criando um método construtor

        def __init__(self):
            Animal.__init__(self) # chamando o método construtor da classe pai
            print("Porco criado")
    
        
        def barulho(self):
            print("O porco faz o barulho: OINK OINK")

class Galo(Animal):
     
        # criando um método construtor
        def __init__(self):
            Animal.__init__(self) 
            print("Galo criado")
    
        
        def barulho(self):
            print("O galo faz o barulho: CÓCÓCÓ")


# criando um objeto da classe porco, que possui o método barulho herdado da classe animal e sobrescrito na classe porco.
porco = Porco()
porco.mostrar() # o que vale é o método herdado da classe pai, pois não foi sobrescrito na subclasse.
porco.barulho() # o que vale é o método sobrescrito na subclasse

# criando um objeto da classe galo, que possui o método barulho herdado da classe animal e sobrescrito na classe galo.
galo = Galo()
galo.mostrar()
galo.barulho()

# criando um objeto da classe animal, que não possui o método barulho
animal = Animal()
animal.mostrar()
animal.barulho()
