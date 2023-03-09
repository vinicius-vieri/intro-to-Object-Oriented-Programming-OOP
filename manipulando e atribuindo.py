"""Em Python, podemos manipular os atributos de um objeto por meio de atribuição direta ou por meio de métodos. 
Para atribuição direta, basta acessar o atributo e atribuir um novo valor a ele."""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando um objeto Pessoa
p = Pessoa("Vinicius",21)

# Acessando e alterando o atributo idade diretamente
p.idade = 22

# Imprimindo
print(p.idade)

"""Porém, em Python, também podemos criar métodos para manipular os atributos de um objeto."""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método para alterar o atributo idade
    def alterar_idade(self, idade):
        self.idade = idade


# Criando um objeto Pessoa
p = Pessoa("Vinicius",21)

# Imprimindo
print(p.idade)

# Alterando o atributo idade
p.alterar_idade(22)

# Imprimindo novamente
print(p.idade)

"""Agora, vamos criar um método para alterar o atributo nome.
O método alterar_nome deve receber como parâmetro o novo nome e alterar o atributo nome do objeto."""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método para alterar o atributo idade
    def alterar_idade(self, idade):
        self.idade = idade

    # Método para alterar o atributo nome
    def alterar_nome(self, nome):
        self.nome = nome

# Criando um objeto Pessoa
p = Pessoa("Vinicius",21)

# Imprimindo
print(p.nome)

# Alterando o atributo nome
p.alterar_nome("João")

# Imprimindo novamente
print(p.nome)
