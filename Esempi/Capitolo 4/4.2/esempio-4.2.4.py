# Uso dell'istruzione continue con while

max = int(input())
numero = 1
while numero <= max:
    if numero == 17:
       continue
    print("Numero:", numero)
    numero += 1
print("programma terminato") 