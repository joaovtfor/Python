lista = [9, 32, 7, 55, 15]
valor = 7
valor2 = 30
valorUsuário = int(input("Digite um valor: "))

def encontrar_valor(lista, valor):
    for elemento in lista:
        if elemento == valor:
            print("Valor encontrado")
            return True
    print("Valor não encontrado")
    return False

print("Saída:")
print("Lista = [9, 32, 7, 55, 15]")
print("================================================")
print("Valor = 7")
print(encontrar_valor(lista, valor))
print("================================================")
print("Valor = 30")
print(encontrar_valor(lista, valor2))
print("================================================")
print(f"Valor digitado: {valorUsuário}")
print(encontrar_valor(lista, valorUsuário))