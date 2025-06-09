# Verificare se la stringa "info@example.com" termina con la sottostringa "@gmail.com" e stampare "Indirizzo gmail" in caso affermativo.
# Riscrivere tutti gli esercizi precedenti usando una funzione
def verifica_gmail():
    s = "info@example.com"
    if s.endswith("@gmail.com"):
        print("Indirizzo gmail")

verifica_gmail()
