par = 0
num = 0
intervalo = 0
soma = 0

while num < 102:
    print(num)
    num += 2
    if num % 2 == 0:
        par += 1
        soma += num
print(f"Há {par} números pares")
print(f"A soma dos números pares é: {soma}")
        