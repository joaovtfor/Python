import random

palavras_secretas = []
arquivo = open('palavras.txt', 'r')
# readlines() é utilizado para ler todas as linhas de um arquivo de texto e retorná-las como uma lista de strings
palavras = arquivo.readlines()

for palavra in palavras:
    # rstrip() é utilizado para remover o caractere de nova linha "\n" que é adicionado ao final de cada palavra lida do arquivo.
    palavra = palavra.rstrip('\n')
#   print(palavra)
    # append() é utilizado para adicionar cada palavra lida do arquivo "palavras.txt" à lista "palavras_secretas".
    palavras_secretas.append(palavra)
arquivo.close()

print(palavras_secretas)
palavra_secreta = random.choice(palavras_secretas)

digitadas = []
chances = 5

while True:
    letra = str(input('Digite uma letra: ').lower())
                
    #Permitir jogar uma letra de cada vez            
    if len(letra) > 1:
        print ('É permitido digitar apenas uma letra por vez')
        continue

    if letra in digitadas:
        print('Você já digitpalavra_secretaou essa letra antes')
        continue
    
    # Inserir letra digitada na lista (digitadas = [])
    digitadas.append(letra)
    #Se estiver a letra na palavra secreta ela é adicionada a uma string temporária que contém todas as letras que o usuario acertou.
    #Se não estiver, o número de chances restantes é reduzido.
    temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            temporario += letra_secreta
        else:
            temporario += '*'
    
    #Verifica se o usuario acertou a palavra secreta comparando a string temporária com a palavra secreta original
    if temporario == palavra_secreta:
        print ('Acertou! Parabéns!')
        break
    else:
        #Mostra como está ficando a palavra secreta
        print ('A palavra secreta está assim', temporario)

    #Diminui as chances
    if letra not in palavra_secreta:
        chances -= 1
    
    if chances <= 0:
        print('Você perdeu !!')
        print('Palavra secreta',palavra_secreta)
        break
    
    print ('Você ainda tem',chances,'chances.')