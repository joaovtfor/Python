import random

jogada = input("Pedra, papel ou tesoura? ")
possblty = ["pedra", "papel", "tesoura"]

if jogada == "pedra" or jogada== "papel" or jogada == "tesoura":
    aleatorio = random.choice(possblty)
    if jogada == "pedra" and aleatorio == "pedra":
        print(f"Jogada adversária: {aleatorio}")
        print("Empate, jogue novamente!")
    elif jogada =="pedra" and aleatorio == "papel":
        print(f"Jogada adversária: {aleatorio}")
        print("Você perdeu!")
    elif jogada =="pedra" and aleatorio == "tesoura":
        print(f"Jogada adversária: {aleatorio}")
        print("Você ganhou!")
    elif jogada == "papel" and aleatorio == "pedra":
        print(f"Jogada adversária: {aleatorio}")
        print("Você ganhou!")
    elif jogada =="papel" and aleatorio == "papel":
        print(f"Jogada adversária: {aleatorio}")
        print("Empate, jogue novamente!")
    elif jogada =="papel" and aleatorio == "tesoura":
        print(f"Jogada adversária: {aleatorio}")
        print("Você perdeu!")
    elif jogada == "tesoura" and aleatorio == "pedra":
        print(f"Jogada adversária: {aleatorio}")
        print("Você perdeu!")
    elif jogada =="tesoura" and aleatorio == "papel":
        print(f"Jogada adversária: {aleatorio}")
        print("Você ganhou!")
    elif jogada =="tesoura" and aleatorio == "tesoura":
        print(f"Jogada adversária: {aleatorio}")
        print("Empate, jogue novamente!")
else:
    print("Jogada inválida")
