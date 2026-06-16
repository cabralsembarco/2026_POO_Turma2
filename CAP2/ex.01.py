class Viagem:
    def __init__(self):
        self.__id = 1
        self.__distancia = 0.0
        self.__litros = 0.0
        self.__tempo = 0.0

    def set_id(self, id):
        if id < 0:
            raise ValueError("ID deve ser positivo")
        else:
            self.__id = id

    def set_distancia(self, dist):
        if dist >= 0:
            self.__distancia = dist
        else:
            raise ValueError("Distância inválida")

    def set_litros(self, lit):
        if lit > 0:
            self.__litros = lit
        else:
            raise ValueError("Litros inválidos")
    
    def set_tempo(self, tempo):
        if tempo > 0:
            raise ValueError("Tempo não pode ser negativo")
        else:
            self.__tempo = tempo

    def get_id(self):
        return self.__id

    def get_distancia(self):
        return self.__distancia

    def get_litros(self):
        return self.__litros
    
    def get_tempo(self):
        return self.__tempo

    def calc_consumo(self):
        return self.__distancia / self.__litros


class UI:
    viagens = []
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1: UI.viagem()
            if op == 2: UI.inserir()
            if op == 3: UI.listar()


    @staticmethod
    def menu():
        print("1-Calcular 2-Inserir 3-Listar 4-Fim")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def viagem():
        print("Cálculo do consumo médio de combustível")
        x = Viagem()
        x.set_id = int(input("ID: "))
        x.set_distancia = (float(input("Distância: ")))
        x.set_litros = (float(input("Litros: ")))
        consumo = x.calc_consumo()
        print(
            f"Viagem para {x.get_destino()} | "
            f"Distância: {x.get_distancia()} km | "
            f"Litros: {x.get_litros()} L | "
            f"Consumo: {consumo:.2f} km/L"
        )

    @classmethod # @classmethod serve para chamar uma lista fora da função
    def inserir(cls):
        x = Viagem()
        x.set_id(int(input("Informe o ID da viagem: ")))
        x.set_distancia(float(input("Informe a distância em km: ")))
        x.set_tempo(float(input("Informe o tempo: ")))
    
    @classmethod
    def listar(cls):
        if len(cls.viagem) == 0:
            print("nenhuma viagem registrada")

UI.main()