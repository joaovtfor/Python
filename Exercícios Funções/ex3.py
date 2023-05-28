def validacao(var1):
    if var1 > 0:
        print(f"O número {var1} é positivo")
    elif var1 < 0:
        print(f"O número {var1} é negativo")
    else:
        print("O número é zero")
    return validacao

num = int(input("Digite um número: "))

print(validacao(num))