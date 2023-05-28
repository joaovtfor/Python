nota1 = int(input("Digite sua primeira nota"))
nota2 = int(input("Digite sua segunda nota"))
nota3 = int(input("Digite sua terceira nota"))
nota4 = int(input("Digite sua quarta nota"))

media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 7:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")