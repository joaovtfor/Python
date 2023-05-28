var5 = ["Algoritmos,", "WebLab", "Cibercultura", "Robótica"]

def media( var1, var2, var3, var4, var5):
    if var5 == "Algoritmos":
        var1 = var1 * 2
        var2 = var2 * 3
        var3 = var3 * 4
        var4 = var4 * 5
        media_geral = (var1 + var2 + var3 + var4) / 14
    elif var5 == "WebLab":
        var1 = var1 * 5
        var2 = var2 * 4
        var3 = var3 * 3
        var4 = var4 * 2
        media_geral = (var1 + var2 + var3 + var4) / 14
    elif var5 == "Cibercultura":
        var1 = var1 * 5
        var2 = var2 * 3
        var3 = var3 * 4
        var4 = var4 * 2
        media_geral = (var1 + var2 + var3 + var4) / 14
    elif var5 == "Robótica":
        var1 = var1 * 2
        var2 = var2 * 4
        var3 = var3 * 3
        var4 = var4 * 5
        media_geral = (var1 + var2 + var3 + var4) / 14
    else:
        print("Essa matéria não está listada")
    return media_geral

print("================================================================")
print(f"Opções de matéria: {var5}")
print("================================================================")
materia = input("Qual a matéria escolhida? ")
nota1 = float(input("Qual foi sua primeira nota? "))
nota2 = float(input("Qual foi sua segunda nota? "))
nota3 = float(input("Qual foi sua terceira nota? "))
nota4 = float(input("Qual foi sua quarta nota? "))

print(media(nota1, nota2, nota3, nota4, materia))