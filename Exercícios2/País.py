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
        self.__nome
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
    def get_populacao(self)
        return self.__populacao
    def get_area(self):
        return self.__area
    def densidade(self):
        return self.__populacao / self.__area
    
class PaisUI:
    paises = []
    @staticmethod
    def main():
        op = 0
        while op != 7:
            if op == 1: PaisUI.inserir()
            if op == 2: PaisUI.listar()
            if op == 3: PaisUI.atualizar()
            if op == 4: PaisUI.excluir()
            if op == 5: PaisUI.maispopuloso()
            if op == 6: PaisUI.maispovoado()


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
        