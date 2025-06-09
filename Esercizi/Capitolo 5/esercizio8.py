# Contare quante volte compare la sottostringa "abc" nella stringa "abcabcabcabc".
# Stampare "Trovato" se c'è almeno un'occorrenza.
s = "abcabcabcabc"
count = s.count("abc")
if count > 0:
    print("Trovato")
