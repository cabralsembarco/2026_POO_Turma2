class Profissional:
    def __init__(self, id, nome, email, esp):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_esp(esp)

    def set_id(self, id):
        if id < 0: raise ValueError("ID deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome

    def set_email(self, email):
        if email == "": raise ValueError("E-mail deve ser informado")
        self.__email = email

    def set_esp(self, esp):
        if esp == "": raise ValueError("Especialização deve ser informada")
        self.__esp = esp

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_esp(self): return self.__esp

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__esp}"

    def to_json(self):
        return { "id":self.__id, "nome":self.__nome, "email":self.__email, "esp":self.__esp }

    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["email"], dic["esp"])