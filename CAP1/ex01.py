class Produto: # A classe é um tipo de variável
    def __init__(self):
        self._id = 1
        self._nome = ""
        self._preco = 0.0
        self._avaliacao = 1
    def set_id(self, id):
        if id < 0: raise ValueError("ID deve ser positivo")
        self._id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("ID não pode ser vazio")
        self._nome = nome
    def set_preco(self, preco):
        if preco < 0: raise ValueError("Preço deve ser positivo")
        self._preco = preco
    def set_avaliacao(self, avaliacao):
        if avaliacao < 1 or avaliacao > 5: raise ValueError("Avaliação deve ser de 1 a 5")
        self._avaliacao = avaliacao
    def get_id(self):
        return self._id
    def get_nome(self):
        return self._nome
    def get_preco(self):
        return self._preco
    def get_avaliacao(self):
        return self._avaliacao

# O "_" esconde as informações para que valores impossíveis na prática sejam realizados

# Desta forma é necessário um set (para alterar os dados) e um get (que permite ver o valor guardado) para cada variável

a = Produto() # Nome da seguido de () chama o __init__
#a.id = 5
#a.nome = "Café Clássico em Grãos"
#a.preco = -10.0
#a.avaliacao = 5

a.set_id(5)
a.set_nome("Café Clássico em Grãos")
a.set_preco(10)
a.set_avaliacao(5)

print(a.get_id())
print(a.get_nome())
print(a.get_preco())
print(a.get_avaliacao())

# "Há variáveis dentro de uma variável"