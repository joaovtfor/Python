num1 = int(input("Insira um primeiro número: "))
num2 = int(input("Insira um segundo número: "))
num3 = int(input("Insira um terceiro número: "))

if num1 > (num2 and num3):
    print("O primeiro número é maior")
elif num2 > (num1 and num3):
    print("O segundo número é maior")
elif num3 > (num1 and num2):
    print("O terceiro número é maior")
elif (num3 == num2 == num1):
    print("Todos os números são iguais")