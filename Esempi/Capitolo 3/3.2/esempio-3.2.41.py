try:
   dividendo = int(input())
   divisore = int(input())
   risultato = dividendo / divisore
except ( ValueError, ZeroDivisionError ) as error: 
   print("Valore inserito non valido:", error)
