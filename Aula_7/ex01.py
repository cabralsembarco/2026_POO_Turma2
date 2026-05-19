from datetime import datetime
s = input("Infore sua data de nascimento no formato dd/mm/aaaa: ")
print(s)
d, m, a = s.split("/")

d = int(d)
m = int(m)
a = int(a)
print(d)
print(m)
print(a)
data = datetime(d, m, a)
print(data)
print(data.strftime("%d/%m/%Y")) # - strftime passa uma data para a string