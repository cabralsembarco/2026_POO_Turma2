print("Digite uma sequência de números separados por vírgula:")
x = input()
v = 0

s = x.split(",")
for e in s:
    v += int(e)

print(v)