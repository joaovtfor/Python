def soma(var1,var2):
    imc = var1 / (var2 * var2)
    return imc

peso = int(input("Qual é seu peso? "))
altura = float(input("Qual é sua altura? "))

print(f"Seu IMC é: {soma(peso, altura)}")