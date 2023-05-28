print("Digite um número: ")
num1 = int(input())
print("Digite outro número: ")
num2 = int(input())

soma = num1 + num2
div = num1 / num2
prod = num1 * num2
sub = num1 - num2

print("A soma é: ",soma)
print("A subtração é: ",sub)
print("A multiplicação é: ",prod)
print("A divisão é: ",div)

prodf = sub * div
if prodf < prod:
    soma2 = prodf + num1
    print(soma2)