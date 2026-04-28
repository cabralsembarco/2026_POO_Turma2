class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0

    def set_base (self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()

    def set_altura(self, v):
        if v >=0: self.__h = v
        else: raise ValueError

    def get_base(self):
        return self.__b

    def get_altura(self):
        return self.__h

    def calc_area(self):
        return self.__b * self.__h

class Circulo:
    def __init__(self):
        self.__r = 0.0

    def set_raio(self, v):
        if v >= 0:
            self.__r = v
        else:
            raise ValueError()
        return None

    def get_raio(self):
        return self.__r

    def calc_area(self):
        pi = 3.14
        return pi * self.__r ** 2

    def calc_circunferencia(self):
        pi = 3.14
        return 2 * pi * self.__r
    
class Viagem:
    def __init__(self):
        self.__km = 0.0
        self.__t = 0.0

    def set_km(self, v):
        if v >= 0:
            self.__km = v
        else:
            raise ValueError()
        return None
    
    def set_tempo(self, v):
        if v >= 0:
            self.__t = v
        else:
            raise ValueError()
        return None
    
    def get_km(self):
        return self.__km
    
    def get_tempo(self):
        return self.__t
    
    def calc_media(self):
        return self.__km / self.__t
    
class Conta:
    def __init__(self):
        self.__nome: str = ""
        self.__numero = 0
        self.__saldo = 0.0
    def set_nome(self, v):
       self.__nome = v
       return None
        
    def set_numero(self, v):
        if v >= 0:
            self.__numero = v
        else:
            raise ValueError()
        return None
        
    def set_saldo(self, v):
        if v >= 0.0:
            self.__saldo = v
        else:
            raise ValueError()
        return None
        
    def get_nome(self):
        return self.__nome
    
    def get_numero(self):
        return self.__numero
    
    def get_saldo(self):
        return self.__saldo
    
    def calc_deposito(self, v):
        if v >= 0.0:
            return v
        else:
            raise ValueError()
        return self.__saldo + v
    
    def calc_saque(self, v):
        if v >= 0.0 and v <= self.__saldo:
            return v
        else:
            raise ValueError()
        return self.__saldo - v and v
    


class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.conta()

    @staticmethod
    def menu():
        print("1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária 5-Ingresso 9-Fim")
        op = int(input("Escolha uma opção: "))
        return op
    
    @staticmethod
    def triangulo():
        print("Calculo da área do trinângulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))
        x.set_altura(float(input("Informe o valor da altura: ")))
        area = x.calc_area()
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}")

    @staticmethod
    def circulo():
        print("1-Cáculo da área 2-Cálculo da circunferência")
        ty = int(input("Selecione qual calculo deseja fazer: "))
        if ty == 1:
            x = Circulo()
            x.set_raio(float(input("Informe o valor do raio: ")))
            area = x.calc_area()
            print(f"Um círculo de raio {x.get_raio()} tem área {area}")
        elif ty == 2:
            x = Circulo()
            x.set_raio(float(input("Informe o valor do raio: ")))
            circun = x.calc_circunferencia()
            print(f"Um círculo de raio {x.get_raio()} tem área {circun}")

    @staticmethod
    def viagem():
        x = Viagem()
        x.set_km(float(input("Informe o valor de km: ")))
        x.set_tempo(float(input("Informe o valor de horas: ")))
        viagem = x.calc_media()
        print(f"Uma viagem com {x.get_km()} que dura {x.get_tempo()} tem uma média de velocidade de {viagem}")
    
    @staticmethod
    def conta():
        x = Conta()
        x.set_nome(input("Informe o nome do cliente: "))
        x.set_numero(int(input("Informe o número da conta: ")))
        x.set_saldo(float(input("Informe o saldo da conta: ")))
        print("1-Depósito 2-Saque")
        ty = int(input("Selecione qual operação deseja fazer: "))
        if ty == 1:
            valor = float(input("Informe o valor do depósito: "))
            deposito = x.calc_deposito(valor)
            print(f"O valor do depósito atual é de {deposito}")
        elif ty == 2:
            valor = float(input("Informe o valor do saque: "))
            saque = x.calc_saque(valor)
            print(f"O valor do saque atual é de {saque}")




UI.main()