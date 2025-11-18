# Esempio di concatenazione di liste

lista = [3, "ciao", 4.0]
lista.extend([1, 2, 1])  # Adesso lista contiene [3, "ciao", 4.0, 1, 2, 1]
print(lista)

lista2 = [3, "ciao", 4.0]
lista2 = lista2 + [1, 2, 1]  # Adesso lista2 contiene [3, "ciao", 4.0, 1, 2, 1]
print(lista2)       