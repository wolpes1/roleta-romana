grupo_pessoas = ["John", "Bea", "Lyncoln", "Christopher", "Rudolf", "Lyr"]

contador_passos = 0

passo = 2

print(grupo_pessoas)

def matar(grupo, posicao):
    print(f"{grupo[posicao]} morreu!")
    grupo.pop(posicao)

while len(grupo_pessoas) != 1:
    print(f"O grupo de pessoas contém {len(grupo_pessoas)} ainda.")
    contador_passos += passo
    if contador_passos > len(grupo_pessoas):
        contador_passos -= len(grupo_pessoas)
    matar(grupo_pessoas, contador_passos)

print(f"A única pessoa sobrevivente é {grupo_pessoas[0]}")

