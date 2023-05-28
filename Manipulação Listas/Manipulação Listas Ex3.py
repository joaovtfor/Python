listMain = []
listNames = []
listMain = []
contador = 0
comandos = [1,2,3,4,5,6]

print("MENU DE OPÇÕES")
print("1 - Tamanho da lista")
print("2 - Inserir nomes")
print("3 - Pesquisar nome")
print("4 - Excluir nome da lista")
print("5 - Exibir lista")
print("6 - Sair")

while True:
    print("-----------------------------------------")
    opt = int(input("Informe a opção que deseja executar: "))
    if opt == 1:
        listaLength = int(input("Informe o tamanho da lista: "))
    elif opt == 2:       
        while len(listMain) < listaLength:
            listNames = input(f"Insira o nome {contador}: ")
            contador += 1
            listMain.append(listNames)
    elif opt == 3:
        search = str(input("Informe o nome que deseja pesquisar: "))
        if search in listMain:
            print("Nome localizado.")
        else:
            print("Nome não localizado")
    elif opt == 4:
        remv = str(input("Informe o nome que deseja excluir: "))
        if remv in listMain:
            listMain.remove(remv)
            print(f"O nome {remv} foi excluído da lista")
        else:
            print("Nome não encontrado")
    elif opt == 5:
        print(listMain)
    elif opt == 6:
        print("-----------------------------------------")
        print("FINALIZADO")
        break
    else:
        print("Comando não encontrado")