class Pais:
    def __init__(self, id, nome, populacao, area):
        self.set_id(id)
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)

    def set_id(self, id):
        if id < 0:
            raise ValueError("O ID não pode ser negativo")
        self.__id = id

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("O nome não pode ser vazio")
        self.__nome = nome

    def set_populacao(self, populacao):
        if populacao < 0:
            raise ValueError("Um país não pode ter uma população negativa")
        self.__populacao = populacao

    def set_area(self, area):
        if area < 0:
            raise ValueError("Um país não pode ter uma área negativa")
        self.__area = area

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_populacao(self):
        return self.__populacao
    
    def get_area(self):
        return self.__area
    
    def densidade(self):
        return self.__populacao / self.__area
    
    def __str__(self):
        return f"{self.__id} - {self.__nome} | População: {self.__populacao} | Área: {self.__area}"

class PaisUI:
    paises = []
    @staticmethod
    def main():
        op = 0
        while op != 3:
            op = PaisUI.menu()
            if op == 1: PaisUI.inserir()
            elif op == 2: PaisUI.listar()
            elif op == 3: PaisUI.atualizar()
            elif op == 4: PaisUI.excluir()
            elif op == 5: PaisUI.maispopuloso()
            elif op == 6: PaisUI.maispovoado()


    @staticmethod
    def menu():
        print("1-Inserir 2-Listar 3-Atualizar 4-Excluir 5-MaisPopuloso 6-MaisPovoado 7-Fim")
        return int(input("Escolha uma ação: "))
    
    @classmethod
    def inserir(cls):
        id = int(input("Digite o ID do país: "))
        nome = input("Digite o nome do país: ")
        populacao = int(input("Informe o número de habitantes do país: "))
        area = float(input("Informe a área do país: "))
        x = Pais(id, nome, populacao, area)
        cls.paises.append(x)

    @classmethod
    def listar(cls):
        if len(cls.paises) == 0:
            print("Nenhum país registrado")
        else:
            for x in cls.paises:
                print(x)

    @classmethod
    def atualizar(cls):
        if len(cls.paises) == 0:
            print("Nenhum país registrado")
            return
        for i, pais in enumerate(cls.paises, start=1):
            print(f"{i} - {pais.get_nome()}")
        att = int(input("Escolha o país para atualizar: "))
        while att < 1 or att > len(cls.paises):
            att = int(input("Escolha um número válido: "))
    
        pais = cls.paises[att - 1]
    
        nome = input("Novo nome: ")
        populacao = int(input("Nova população: "))
        area = float(input("Nova área: "))
    
        pais.set_nome(nome)
        pais.set_populacao(populacao)
        pais.set_area(area)
    
        print("País atualizado com sucesso.")

    @classmethod
    def excluir(cls):
        if len(cls.paises) == 0:
            print("Nenhum país registrado")
            return
        for i, pais in enumerate(cls.paises, start=1):
            print(f"{i} - {pais.get_nome()}")
        att = int(input("Escolha o país para excluir: "))
        while att < 1 or att > len(cls.paises):
            att = int(input("Escolha um número válido: "))
    
        removido = cls.paises.pop(att - 1)

        print(f"{removido.get_nome()} foi removido")

    @classmethod
    def maispopuloso(cls):
        if len(cls.paises) == 0:
            print("Nenhum país registrado")
            return
        for i, pais in enumerate(cls.paises, start = 1):
            print(f"{pais.get_nome} é o mais populoso")


PaisUI.main()