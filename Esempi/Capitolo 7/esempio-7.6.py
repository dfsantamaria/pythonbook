# Esempio sull'uso di alcuni metodi della lista

lista = [3, "ciao", 4.0, 12]
print(len(lista))

lista.remove("ciao")  # Cerca e rimuove "ciao" dalla lista

lista.pop(0)  # Elimina l'elemento in posizione 0 dalla lista

lista.append("ciao")  # Inserisce "ciao" in fondo alla lista

lista.insert(1, 5)  # Inserisce 5 nella posizione 1 della lista

lista.count("ciao")  # Conta le occorrenze di 'ciao' nella lista

lista.copy()  # Restituisce una copia della lista

lista.clear()  # svuota la lista