# Verificare se la stringa "Python" è composta solo da lettere oppure se da caratteri alfanumerici.
# Stampare a schermo "Solo lettere" nel primo caso, "Lettere e numeri" nel secondo.
s = "Python"
if s.isalpha():
    print("Solo lettere")
elif s.isalnum():
    print("Lettere e numeri")
