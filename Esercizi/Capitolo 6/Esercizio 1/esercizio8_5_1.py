# Contare quante volte compare la sottostringa "abc" nella stringa "abcabcabcabc". Stampare "Trovato" se c'è almeno un'occorrenza.
# Riscrivere tutti gli esercizi precedenti usando una funzione
def conta_abc():
    s = "abcabcabcabc"
    count = s.count("abc")
    if count > 0:
        print("Trovato")

conta_abc()
