def stampa_tutti(messaggio, *tupla, altro_messaggio):
   print(messaggio)
   for elem in tupla:
       print(elem)
   print(altro_messaggio)
#Fine della definizione della funzione

stampa_tutti("Elenco:", 1,2,3,4,5, altro_messaggio="Fine elenco")