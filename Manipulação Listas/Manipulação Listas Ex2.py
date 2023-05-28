listaP = ["Brasil", "Argentina", "Uruguai", "Paraguai"]
contador1 = listaP.count("Paraguai")
contador2 = listaP.count("França")

print(f"Lista atual: {listaP}")
print(f"Foram encontrados {len(listaP)} elementos na lista original")
print(f"Foi encontrada {contador1} de *Paraguai* na lista original.")
print(f"O terceiro elemento encontrado na lista original foi: {listaP[2]}")
listaP.insert(2, "México")
print(f"Foi adicionado México no índice 2 da lista original: {listaP}")
listaP.sort()
print(f"Nova lista ordenada: {listaP}")
print(f"O país *França* foi localizado na lista: {contador2}")
listaP.remove("Brasil")
print(f"O país *Brasil* foi removido da lista: {listaP}")
listaP.reverse()
print(f"A lista foi invertida: {listaP}")