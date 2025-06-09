# Stampare a schermo i numeri compresi tra x e y interropendo la stampa se il valore è z.
# x,y,z devono essere inseriti dall'utente.
x = int(input("Inserisci x: "))
y = int(input("Inserisci y: "))
z = int(input("Inserisci z: "))

i = x
while i <= y:
    if i == z:
        break
    print(i)
    i += 1
