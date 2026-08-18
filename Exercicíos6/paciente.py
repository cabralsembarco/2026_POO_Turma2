from datetime import datetime as dt

class Paciente:
    def __init__(self, nome, cpf, fone, nasc):
        self.__nome = nome
        self.__cpf = cpf
        self.__fone = fone
        self.__nasc = nasc
    def __str__(self):
        return f"{self.__nome} - {self.__cpf} - {self.__fone} - {self.__nasc.strftime('%d/%M/%Y')}
    def idade(self):
        x = dt.now() - self.__nasc
        dias = x.days
        anos = dias // 365
        meses = dias % 365 // 30
        return f"{anos} ano(s) e {meses} mes(es)"