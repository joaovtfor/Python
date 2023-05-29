alimento = input("Digite um produto da lista de compras: ")
lista = ['Arroz', 'Queijo', 'Pão', 'Café']
print("--------------------")

def encontrar_produto(lista, produto):
    for elemento in lista:
        if elemento == produto:
            return f"O produto {produto} está na lista de compras!"
        else:
            return "Produto não encontrado!"

print(encontrar_produto(lista, alimento))
print("---------------------------")