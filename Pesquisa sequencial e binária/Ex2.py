num = 0
lista = []
print("Digite 5 valores: ")
print("---------------------------------")

for i in range(5):
    num += 1
    valor = int(input(f"Valor {num}: "))
    print("---------------------------------")
    lista.append(valor)

def encontrar_maior(lista, valor):
    for elemento in lista:
        if elemento >= valor:
            return elemento
    
print(f"O maior valor é: {encontrar_maior(lista, valor)}")