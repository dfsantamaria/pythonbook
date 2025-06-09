# Definizione di una funzione

def pulisci_stringa(mia_stringa):
    mia_stringa = mia_stringa.replace(' ', '')
    for c in mia_stringa:
        if c.isdecimal():
            return mia_stringa
    mia_stringa = mia_stringa.capitalize()
    return mia_stringa