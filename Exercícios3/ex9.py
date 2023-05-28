import random

numPC = random.randint(1,10)
chances = 0

while (chances < 3):
    num = int(input("Digite um número: "))
    if num == numPC:
        if num == numPC:
            print("Você venceu!")
            break
        elif chances == 3:
            print("Você perdeu!")
    else:
        chances += 1
        print("Tente novamente!")