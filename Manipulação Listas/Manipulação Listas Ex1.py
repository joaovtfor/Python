lista1 = ["Abacate", "Maçã","Banana", "Abacaxi", "Ameixa", "Goiaba"]
lista2 = [1, 2, 123, 3, 1234, 4, 4, 4, 4, 4, 4, 4]
lista3 = ["Chocolate", 3756, True]

print("MANIPULAÇÃO DE LISTAS")
print("Listas:")
print("--------------------------------------------")

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}")
print("--------------------------------------------")

print("Manipulação 1 (min, max, sum) - lista2")
print(min(lista2))
print(max(lista2))
print(sum(lista2))
print("--------------------------------------------")

print("Manipulação 2 (len) - lista1")
print(len(lista1))
print("--------------------------------------------")

print("Manipulação 3 (count) - lista2")
print(lista2.count(4))
print("--------------------------------------------")

print("Manipulação 4 (append) - lista1 ")
lista1.append("Pêssego")
print (lista1)

print("Manipulação 5 (insert) - lista2")
lista2.insert(2, 999)
print(lista2)
print("--------------------------------------------")

print("Manipulação 6 (remove) - lista1")
print(lista1)
lista1.remove("Pêssego")
print(lista1)
print("--------------------------------------------")

print("Manipulação 7 (pop) - lista2")
print(lista2)
lista2.pop(2)
print(lista2)
print("--------------------------------------------")

print("Manipulação 8 (clear) lista3")
print(lista3)
lista3.clear()
print(lista3)
print("--------------------------------------------")

print("Manipulação 9 (sort) - lista1")
print(lista1)
lista1.sort()
print(lista1)
print("--------------------------------------------")

print("Manipulação 10 (reverse) lista1")
print(lista1)
lista1.reverse()
print(lista1)
print("--------------------------------------------")