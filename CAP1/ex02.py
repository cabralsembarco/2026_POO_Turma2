class Produto:
    def __init__(self, id, nome, preco, avaliacao): # Desta forma a classe já começa com dados predefinidos, e que podem ser mudados
        self.set_id(id)
        self.set_nome(nome)
        self.set_preco(preco)
        self.set_avaliacao(avaliacao)
    def __str__(self): # Muda a mensagem que aparece no print (<_main_...>)
        return f"{self.set_nome} - ID: {self.set_id} - Preço: {self.set_preco} - Avaliação: {self.set_avaliacao}"
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


a = Produto(5, "Café Clássico em Grãos", 10, 5)

a.set_id(5)
a.set_nome("Café Clássico em Grãos")
a.set_preco(10)
a.set_avaliacao(5)

print(a.get_id())
print(a.get_nome())
print(a.get_preco())
print(a.get_avaliacao())

print(a)

# "Há variáveis dentro de uma variável"