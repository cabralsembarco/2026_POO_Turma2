print("Insira um número à sua escolha:")
x = int(input())
print("Insira mais um:")
y = int(input())

def maior(x, y):
    if x > y:
        print("O maior número é:", x)
    elif y > x:
        print("O maior número é:", y)
    elif x == y:
        print("Números iguais")

maior(x, y)