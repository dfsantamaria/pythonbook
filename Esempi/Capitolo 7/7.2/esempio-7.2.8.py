# Esempio di unpacking di una tupla come argomento di una funzione

def somma(a, b, c):
    return a + b + c
tupla = (1, 2, 3)
print(somma(*tupla))  # equivale a somma(1, 2, 3)