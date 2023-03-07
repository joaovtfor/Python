#print("Informe um número:")
#numero = input()
#print("O número informado foi: ",numero)

#print('Informe um número:')
#numero1 = int(input())

#print('Informe outro número')
#numero2 = int(input())

#soma = numero1 + numero2

#print('A soma é: ',soma)

#ano_nascimento = 2002
#print(ano_nascimento)
#print(type(ano_nascimento))

print("Qual é seu nome?")
nome = input()
print("Você realizou a avaliação?(true para sim, false para não)")
avaliacao = str(input())
if avaliacao == 'false':
    print("Vá fazer os testes!")
else:
    print("Qual foi a nota da sua primeira prova?")
    nota1 = int(input())
    print("Qual foi a nota da sua segunda prova?")
    nota2 = int(input())
    notaf = (nota1 + nota2)/2
    notaf = int(notaf)

    if notaf >= 7:
        print("Parabéns,",nome,"! Você passou no teste com média final aproximada:",notaf)
    else:
        print("Infelizmente você reprovou",nome,". Tente novamente!")
    







