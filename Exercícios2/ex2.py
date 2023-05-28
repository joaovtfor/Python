nasc = int(input("Que ano você nasceu? "))
atual = int(input("Em que ano está? "))

idade = atual - nasc

if idade >= 16:
    print(f"Você pode votar, pois você tem {idade} anos")
else:
    print(f"Você não pode votar, pois tem {idade} anos")