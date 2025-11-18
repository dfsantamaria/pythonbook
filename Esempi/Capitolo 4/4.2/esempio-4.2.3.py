# Uso dell'istruzione break con while

max = int(input())
numero = 1
while numero <= max:
    if numero == 17:
       break
    print("Numero: ", numero)
    numero += 1
else:
    print("Il numero sfortunato non è presente!")
print("Programma terminato")  