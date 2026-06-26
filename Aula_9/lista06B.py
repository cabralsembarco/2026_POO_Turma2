from datetime import datetime
import json

class Contato():
    def __init__(self, id, nome, email, fone, data):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_data(data)
    def set_id(self, id):
        if id < 0: raise ValueError("ID deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser nulo")
        self.__nome = nome
    def set_email(self, email):
        if email == "": raise ValueError("Email não pode ser nulo")
        self.__email = email
    def set_fone(self, fone):
        if fone == "": raise ValueError("Telefone não pode ser nulo")
        self.__fone = fone
    def set_data(self, data):
        if isinstance(data, datetime):
            self.__data = data
        elif data > datetime.now(): raise ValueError("Data não pode ser no futuro")
        else: raise ValueError("Digite a data corretamente")

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_data(self): return self.__data
    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__data}"
    
    def to_json(self):
        return { "id":self.__id, "nome":self.__nome, "email":self.__email, "telefone":self.__fone, "data_de_nascimento":self.__data}
    
    @staticmethod
    def from_json(dic):
        return Contato(dic["id"], dic["nome"], dic["email"], dic["telefone"], dic["data_de_nascimento"])
    
class ContatoUI:
    __objetos = []
    @staticmethod
    def main():
        ContatoUI.abrir()
        op = 0
        while op != 9:
            if op == 1: ContatoUI.inserir()
            elif op == 2: ContatoUI.listar()
            elif op == 3: ContatoUI.atualizar()
            elif op == 4: ContatoUI.excluir()
        
    @staticmethod
    def menu():
        print("1-Inserir 2-Listar 3-Atualizar 4-Excluir")
        op = int(input("Escolha uma opção: "))
        return op
    
    @classmethod
    def salvar(cls):
        arquivo = open("contatos.json", mode = "w")
        json.dump(cls.__objetos, arquivo, default = Contato.to_json, indent = 2)
        arquivo.close()
        print("O arquivo contatos.json foi salvo")



    
