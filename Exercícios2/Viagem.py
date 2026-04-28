class Viagem:
    def __init__(self):
        self.__a = ""
        self.__b = 0.0
        self.__c = 0.0

    def set_destino(self, dest):
        if isinstance(dest, str):
            self.__a = dest
        else:
            raise ValueError("Destino inválido")

    def set_distancia(self, dist):
        if dist >= 0:
            self.__b = dist
        else:
            raise ValueError("Distância inválida")

    def set_litros(self, lit):
        if lit > 0:
            self.__c = lit
        else:
            raise ValueError("Litros inválidos")

    def get_destino(self):
        return self.__a

    def get_distancia(self):
        return self.__b

    def get_litros(self):
        return self.__c

    def calc_consumo(self):
        return self.__b / self.__c


class UI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1:
                UI.viagem()

    @staticmethod
    def menu():
        print("1-Calcular 2-Fim")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def viagem():
        print("Cálculo do consumo médio de combustível")
        x = Viagem()
        x.set_destino(input("Destino: "))
        x.set_distancia(float(input("Distância: ")))
        x.set_litros(float(input("Litros: ")))
        consumo = x.calc_consumo()
        print(
            f"Viagem para {x.get_destino()} | "
            f"Distância: {x.get_distancia()} km | "
            f"Litros: {x.get_litros()} L | "
            f"Consumo: {consumo:.2f} km/L"
        )


UI.main()