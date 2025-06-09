# Definizione di funzione con annotazione di tipo

def pulisci_stringa(mia_stringa: str): -> str | None
   mia_stringa = mia_stringa.replace(' ', '')
   for c in mia_stringa:
    if c.isdecimal():
        return None
   mia_stringa = mia_stringa.capitalize()
   return mia_stringa
