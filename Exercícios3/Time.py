class Time:
    def __init__(self, id, nome, estado):
        self.id = id
        self.nome = nome
        self.estado = estado

    def set_id(self, id):
        if id < 0:
            raise ValueError("o ID não pode ser nulo")
        self.id = id

    def set_nome(self, nome):
        if not isinstance(nome, str):
            raise ValueError("Nome inválido")
        self.nome = nome

    def set_estado(self, estado):
        if not isinstance(nome, str):
            raise ValueError("Nome inválido")
        self.estado = estado

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    
    def get_estado(self):
        return self.estado
    
class Jogador:
    def __init__(self, id, idTime, nome, camisa):
        self.id = id
        self.idTime = idTime
        self.nome = nome
        self.camisa = camisa

    def set_id(self, id):
        if id < 0:
            raise ValueError("O ID não pode ser negativo")
        self.id = id

    def set_idTime(self, idTime):
        if idTime < 0:
            raise ValueError("O ID não pode ser nnegativo")
        self.idTime = idTime

    def set_nome(self, nome):
        if not isinstance(nome, str):
            raise ValueError("Nome inválido")
        self.nome = nome

    def set_camisa(self, camisa):
        if camisa < 0:
            raise ValueError("A camisa não pode ter número negativo")
        self.camisa = camisa

    def get_id(self):
        return self.id
    
    def get_idTime(self):
        return self.idTime
    
    def get_nome(self):
        return self.nome
    
    def get_camisa(self):
        return self.camisa

class UI:
    times = []
    jogadores = []
    @staticmethod
    def main():
        op = 0
        t = 0
        j = 0
        while op != 3:
            op = UI.menu()
            if op == 1: 
                t = 0
                while t != 6:
                    t = UI.menuT()
                    if t == 1: UI.inserirT()
                    if t == 2: UI.listarT()
                    if t == 3: UI.atualizarT()
                    if t == 4: 
            elif op == 2:

    @staticmethod
    def menu():
        print("1-Times 2-Jogares")
        return int(input("Escolha uma opção: "))
    
    @staticmethod
    def menuT():
        if
        print("1-Inserir 2-Listar 3-Atualizar 4-Excluir 5-Jogadores 6-Fim")
        return int(input("Escolha uma das ações: "))
    
    @classmethod
    def inserirT(cls):
        id = int(input("Digite o ID do time: "))
        nome = input("Digite o nome do time: ")
        estado = input("Digite o ome do estado: ")
        x = Time(id, nome, estado)
        cls.times.append(x)

    @classmethod
    def listarT(cls):
        if len(cls.times) == 0:
            print("Nenhum time registrado")
            return
        else:
            for x in cls.times:
                print(x)

    @classmethod
    def atualizarT(cls):
        if len(cls.times) == 0:
            print("Nenhum time registrado")
            return
        for i, time in enumerate(cls.times, start = 1):
            print(f"{i} - {time.get_nome()}")
        att = int(input("Escolha o time par atualizar: "))
        while att < 1 or att > len(cls.times):
            att = int(input("Escolha um número válido: "))

        time = cls.times[att - 1]

        id = int(input("Novo ID: "))
        nome = input("Novo nome: ")
        estado = input("Novo estado: ")

        time.set_id(id)
        time.set_nome(nome)
        time.set_estado(estado)

        print("Time atualizado com sucesso")

    @classmethod
    def excluirT(cls):
        if len(cls.times) == 0:
            print("Nenhum time registrado")
            return
        for i, time in enumerate(cls.times):
            print(f"{i} - {time.get_nome()}")
        att = int(input("Escolha o time para excluir: "))
        while att < 0 or att > len(cls.times):
            att = int(input("Escolha um número válido: "))

        removido = cls.times.pop(att - 1)

        print(f"{removido.get_nome()} foi excluído")

    @classmethod
    def listar_jogadores(cls):
        if len(cls.times) == 0:
            print("Nenhum time registrado")
            return
        for i, time in enumerate(cls.times):
            print(f"{i} - {time.get_nome()}")
        att = int(input("Escolha um time para verificar: "))
        while att < 0 or att > len(cls.times):
            att = int(input("Escolha um número válido: "))
        if len(cls.jogadores) == 0:
            print("Nenhum jogador registrado")
            return
        else:
            for i, jogador in enumerate(cls.jogadores):
                print(f"{jogador.get_nome()}")
    
    @staticmethod
    def menuJ():
        print("1-Inserir 2-Listar 3-Atualizar 4-Excluir 5-Transferir 6-Fim")
        return int(input("Escolha uma das ações: "))
    
UI.main()