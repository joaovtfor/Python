preco = float(input("Qual o preço do produto? "))
pag = input("Como será a forma de pagamento? (débito/3 vezes/mais de 3 vezes) ")

if pag == "débito":
    precon = preco * 0.88
    print(f"O preço a se pagar será: {precon}")
elif pag == "3 vezes":
    parcela = preco / 3
    print(f"Cada parcela será de: {parcela}")
elif pag == "mais de 3 vezes":
    precon = preco * 1.15
    print(f"O preço a se pagar será: {precon}")
else:
    print("Forma de pagamento inválida") 