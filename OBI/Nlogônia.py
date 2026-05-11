alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]

consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
               "p", "q", "r", "s", "t", "v", "x", "z"]

vogais = ["a", "e", "i", "o", "u"]

palavra = input("Digite sua palavra: ")

resultado = ""

for letra in palavra:
    if letra in vogais:
        resultado += letra
    elif letra in consoantes:
        pos_letra = alfabeto.index(letra)

        menor_distancia = 999
        vogal_proxima = ""

        for v in vogais:
            pos_vogal = alfabeto.index(v)

            distancia = abs(pos_letra - pos_vogal)

            if distancia < menor_distancia:
                menor_distancia = distancia
                vogal_proxima = v

        pos_consoante = consoantes.index(letra)

        if pos_consoante == len(consoantes) - 1:
            prox_consoante = letra
        else:
            prox_consoante = consoantes[pos_consoante + 1]

        resultado += letra + vogal_proxima + prox_consoante

print("Resultado:", resultado)