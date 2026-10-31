try:
   dividendo = int(input())
   divisore = int(input())
   risultato = dividendo / divisore
except ValueError as value_error: 
   print("Valore inserito non valido:", value_error)
except ZeroDivisionError as zero_error: 
   print("Hai inserito zero come divisore:", zero_error)
