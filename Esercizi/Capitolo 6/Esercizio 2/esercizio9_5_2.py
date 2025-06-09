# Trovare la posizione della parola "cielo" nella stringa "Il sole splende alto nel cielo". 
# Stampare "Alla fine" se si trova a meno di 10 caratteri dalla fine, stampare "All'inizio" altrimenti.
# Riscrivere tutti gli esercizi precedenti usando una funzione da includere in un modulo
def posizione_cielo():
    s = "Il sole splende alto nel cielo"
    pos = s.find("cielo")
    if len(s) - pos < 10:
        print("Alla fine")
    else:
        print("All’inizio")
