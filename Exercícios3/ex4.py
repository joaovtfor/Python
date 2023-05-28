numi = int(input("Digite um valor inicial: "))
numf = int(input("Digite um valor final: "))
intervalo = 0

for intervalo in range(numi,numf +1):
    if numi != numf:
        print(f"O intervalo é: {intervalo}")
    else:
        print("Não é possivel buscar o intervalo de dois valores iguais")