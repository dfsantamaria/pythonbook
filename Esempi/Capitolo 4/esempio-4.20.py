# Uso di for con range e step negativo

stringa = "una stringa"
for posizione in range(len(stringa)-1, -1, -1):
    print(posizione, stringa[posizione])