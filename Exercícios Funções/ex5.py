def verificador(var1, var2, var3, var4, var5, var6, var7, var8):
    contador = 0
    if var1 == (lista_numeros[0], lista_numeros[1], lista_numeros[2], lista_numeros[3],lista_numeros[4], lista_numeros[5], lista_numeros[6], lista_numeros[7]):
        contador += 1

    elif var2 == (lista_numeros[0], lista_numeros[1], lista_numeros[2], lista_numeros[3],lista_numeros[4], lista_numeros[5], lista_numeros[6], lista_numeros[7]):
        contador += 1

    elif var3 == (lista_numeros[0], lista_numeros[1], lista_numeros[2], lista_numeros[3],lista_numeros[4], lista_numeros[5], lista_numeros[6], lista_numeros[7]):
        contador += 1

    elif var4 == (lista_numeros[0], lista_numeros[1], lista_numeros[2], lista_numeros[3],lista_numeros[4], lista_numeros[5], lista_numeros[6], lista_numeros[7]):
        contador += 1

    elif var5 == (lista_numeros[0], lista_numeros[1], lista_numeros[2], lista_numeros[3],lista_numeros[4], lista_numeros[5], lista_numeros[6], lista_numeros[7]):
        contador += 1

    elif var6 == (lista_numeros[0], lista_numeros[1], lista_numeros[2], lista_numeros[3],lista_numeros[4], lista_numeros[5], lista_numeros[6], lista_numeros[7]):
        contador += 1

    elif var7 == (lista_numeros[0], lista_numeros[1], lista_numeros[2], lista_numeros[3],lista_numeros[4], lista_numeros[5], lista_numeros[6], lista_numeros[7]):
        contador += 1

    elif var8 == (lista_numeros[0], lista_numeros[1], lista_numeros[2], lista_numeros[3],lista_numeros[4], lista_numeros[5], lista_numeros[6], lista_numeros[7]):
        contador += 1
        
    return contador

lista_numeros = [35, 5, 25, 85, 15, 95, 55, 65]

print("====================================================")
print("Digite 8 números: ")
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))
num4 = int(input("Número 4: "))
num5 = int(input("Número 5: "))
num6 = int(input("Número 6: "))
num7 = int(input("Número 7: "))
num8 = int(input("Número 8: "))

print(f"Quantidade de números encontrados: {verificador(num1, num2, num3, num4, num5, num6, num7, num8)}")