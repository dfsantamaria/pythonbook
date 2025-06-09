# Uso dell'istruzione break con while

max = int(input())
numero = 1
while numero <= max:
    if numero == 17:
       break
    print("Numero: ", numero)
    numero += 1
print("Programma terminato")