numero = 0
try:
   numero = int(input())
except ValueError: 
   print("Valore inserito non valido")
else:   
   numero += 1
   print(numero)
