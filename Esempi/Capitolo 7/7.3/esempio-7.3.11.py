# Esempio dell'uso del metodo update

dizionario = {"Nome": "Mario", "Cognome": "Rossi", "Matricola": 9999}
dizionario.update(Nome="Giorgio")
dizionario.update({"Cognome": "Bianchi", "Anno": 2025})
dizionario.update((("Cognome", "Bianchini"), ("Anno", 2023)))  