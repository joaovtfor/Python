idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode fazer a carteira AB")
if idade >= 21:
    print("Você pode fazer a carteira D")
if idade < 18:
    print("Você não tem idade para fazer nenhuma carteira")