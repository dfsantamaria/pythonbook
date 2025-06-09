# Verificare se il tipo delle variabili definite dall'esercizio 3) è il tipo string. Stampare a schermo il risultato.
# Riscrivere tutti gli esercizi precedenti usando una funzione.

def verifica_stringhe():
    str1 = "ciao"
    str2 = "mondo"

    sono_stringhe = True

    if not isinstance(str1, str):
        sono_stringhe = False
    if not isinstance(str2, str):
        sono_stringhe = False

    print(sono_stringhe)

verifica_stringhe()
