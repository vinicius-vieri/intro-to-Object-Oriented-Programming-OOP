"""Métodos são funções definidas dentro de uma classe em programação orientada a objetos. 
Eles representam o comportamento de um objeto e permitem que o objeto execute ações e operações específicas.

Em Python, os métodos são definidos dentro de uma classe usando a palavra-chave def seguida pelo nome do método
 e seus parâmetros. Ou seja, um métodos é uma função que está dentro de uma classe"""


class Pessoa:
    # Método construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método para mostrar os dados
    def mostrar(self):
        print("Olá, meu nome é", self.nome, "e tenho", self.idade, "anos.")

    # Método para alterar o nome
    def alterar_nome(self, nome):
        self.nome = nome

    # Método para alterar a idade
    def alterar_idade(self, idade):
        self.idade = idade



# Criando um objeto da classe Pessoa
pessoa = Pessoa("Mauro", 25)

# Chamando o método mostrar
pessoa.mostrar()

# Chamando o método alterar_nome
pessoa.alterar_nome("Ana Lívia")

# Chamando o método mostrar
pessoa.mostrar()

# Chamando o método alterar_idade
pessoa.alterar_idade(59)

# Chamando o método mostrar
pessoa.mostrar()

# Todos os objetos criados a partir da classe Pessoa terão os mesmos métodos, mas os valores de seus atributos serão diferentes.
# O método construtor é definido com o nome __init__ e é chamado automaticamente quando um objeto é criado a partir de uma classe.
# Para definir um valor como default para um atributo, basta atribuir o valor desejado ao atributo dentro do método construtor.
