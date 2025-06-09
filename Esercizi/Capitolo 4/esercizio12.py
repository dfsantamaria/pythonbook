# Stampare a schermo i numeri da x a y in ordine decrescente,
# dove x e y sono letti dall'utente.
x = int(input('Inserisci x: '))
y = int(input('Inserisci y: '))
for i in range(x, y-1, -1):
    print(i)
