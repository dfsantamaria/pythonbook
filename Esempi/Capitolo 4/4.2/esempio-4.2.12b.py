# Uso di for con range senza start e step

stringa = "una stringa"
for posizione in range(len(stringa)-1, -1, -1):
    print(posizione, stringa[posizione])