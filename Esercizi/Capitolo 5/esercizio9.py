# Trovare la posizione della parola "cielo" dalla stringa "Il sole splende alto nel cielo".
# Stampare "Alla fine" se si trova a meno di 10 caratteri dalla fine,
# stampare "All'inizio" altrimenti.
s = "Il sole splende alto nel cielo"
pos = s.find("cielo")
if len(s) - pos < 10:
    print("Alla fine")
else:
    print("All’inizio")
