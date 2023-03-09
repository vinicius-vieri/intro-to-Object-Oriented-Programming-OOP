"""Em Python, uma classe é uma estrutura que define um tipo de objeto. 
Ela é composta por atributos (variáveis) e métodos (funções) que definem 
o comportamento dos objetos criados a partir dessa classe."""


class Pessoa():

    def __init__(self, nome, idade):
      self.nome = nome
      self.idade = idade

    def mostrar(self):
        print("Olá, meu nome é", self.nome, "e tenho", self.idade, "anos.") 



# criando o objeto
pessoa = Pessoa("Vinicius", 21)

# chamando o método
pessoa.mostrar()

#chamando os atributos
print(pessoa.nome)
print(pessoa.idade)


# mas o que é instância de classe, método e atributo?

# instância de classe
"""Uma instância de classe é um objeto criado a partir de uma classe.
No exemplo acima, a variável pessoa é uma instância da classe Pessoa."""

# método
"""Um método é uma função que está dentro de uma classe.
No exemplo acima, o método mostrar() é um método da classe Pessoa."""

# atributo
"""Um atributo é uma variável que está dentro de uma classe.
No exemplo acima, o atributo nome e idade são atributos da classe Pessoa."""

