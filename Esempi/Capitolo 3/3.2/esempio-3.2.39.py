numero = 0
try:
   numero = int(input())
except ValueError as error: 
   print("Valore inserito non valido:", error)
else:   
   numero += 1
   print(numero)
