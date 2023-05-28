import random

words1 = ["Banana", "Maçã", "Abacate", "Laranja", "Pêssego", "Melao", "Mamao", "Melancia", "Pera"]
words2 = ["Processador", "Monitor", "Mouse", "Teclado", "Cooler", "Motherboard", "Memória"]
w_random1 = random.choice(words1)
w_random2 = random.choice(words2)
w_random3 = (w_random1, w_random2)
w_random4 = random.choice(w_random3)

print(w_random4)
print("JOGO DA FORCA")

