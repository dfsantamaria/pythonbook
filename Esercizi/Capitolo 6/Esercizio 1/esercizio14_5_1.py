# Verificare se la stringa "Python" è composta solo da lettere oppure se da caratteri alfanumerici. Stampare "Solo lettere" o "Lettere e numeri".
# Riscrivere tutti gli esercizi precedenti usando una funzione
def verifica_alpha_alnum():
    s = "Python"
    if s.isalpha():
        print("Solo lettere")
    elif s.isalnum():
        print("Lettere e numeri")

verifica_alpha_alnum()
