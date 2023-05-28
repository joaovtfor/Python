peso = float(input("Qual é o seu peso?(em Kg) "))
altura = float(input("Qual é sua altura?(em metro) "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Você está abaixo do peso ideal")
if 18.5 <= imc < 25:
    print("Você está no peso ideal")
if 25 <= imc < 30:
    print("Você está acima do peso ideal")
if 30 <= imc < 35:
    print("Você está com Obesidade Grau I")
if 35 <= imc < 40:
    print("Você está com Obesidade Grau II (severa)")
if imc >= 40:
    print("Você está com Obesidade Grau III (mórbida)")