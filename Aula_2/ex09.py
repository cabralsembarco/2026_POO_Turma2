print("Digite uma frase")
text = input()

s = text.split(" ")
# s = ["palavra1", "palavra2", "palavra3"...]

for e in s:
    e = e[:: -1]
    print(e)