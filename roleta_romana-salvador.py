numero_pessoas = int(input("Quantas pessoas estão no grupo?"))

fila_pessoas = []

contador = 0

passo = int(input("Qual será o passo da morte?"))

while numero_pessoas != 0:
    fila_pessoas.append(numero_pessoas)
    numero_pessoas -= 1

fila_pessoas.reverse()

print(fila_pessoas)

def matar(grupo, posicao):
    print(f"A pessoa da posição {grupo[posicao]} morreu!")
    grupo.pop(posicao)

while len(fila_pessoas) != 1:
    contador += passo
    if contador > len(fila_pessoas):
        contador =- len(fila_pessoas)
    matar(fila_pessoas, contador)

print(f"A posição salva é a {fila_pessoas[0]}.")