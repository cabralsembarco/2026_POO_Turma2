from datetime import datetime
s = input("Infore sua data de nascimento no formato dd/mm/aaaa: ")
data = datetime.strptime(s, "%d/%m/%Y")
print(data)
print(data.strftime("%d/%m/%Y"))

# - strptime passa uma string para datetime
# - strftime passa uma datetime para a string

x = int(input("Informe seu número: "))
d = datetime(input("Informe uma data: "), "%d/%m/%Y")