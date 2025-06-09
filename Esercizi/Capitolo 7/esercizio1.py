# Scrivere una funzione che, presa una lista L di stringhe, restituisca
# una lista che contenga le stringhe di L aventi almeno due “a” in una
# posizione compresa tra 3 e 9.
def stringhe_con_due_a(L):
    for s in L:
        if s[2:9].count('a') >= 2:
            return s

stringa_mia = ["correre", "scappare", "camminare"]
print(stringhe_con_due_a(stringa_mia))