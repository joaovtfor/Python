def comparador_de_valores(var1, var2):
    if var1 > var2:
        print(f"O número {var1} é maior.")
    elif var2 > var1 :
        print(f"O número {var2} é maior.")
    else :
        print("Os números são iguais")
    return comparador_de_valores

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

print(comparador_de_valores(num1, num2))