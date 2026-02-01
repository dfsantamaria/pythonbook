# Chiamata di funzione produttiva e uso di none

nome = "da ni e le"
#Chiamiamo la funzione definita nell'esempio 6.1.7
nuovo_nome = pulisci_stringa(nome)
if nuovo_nome != None:
    nome = nuovo_nome
    print(nome)
else:
    print("Il nome contiene numeri!")