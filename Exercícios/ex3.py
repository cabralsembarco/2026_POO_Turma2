print("Digite uma frase:")
frase = input()
x = 0

for e in frase:
    if e >= '0' and e <= '9':
        x += int(e)

print(x)