print("Digite dois valores inteiros separados por um operador +, -, * ou /")
x = str(input())

def calcular(x):
    if "+" in x:
        v1, v2 = x.split("+")
        print(int(v1) + int(v2))
    elif "-" in x:
        v1, v2 = x.split("-")
        print(int(v1) - int(v2))
    elif "*" in x:
        v1, v2 = x.split("*")
        print(int(v1) * int(v2))
    elif "/" in x:
        v1, v2 = x.split("/")
        print(int(v1) / int(v2))
    else:
        print("Operador inválido")

calcular(x)