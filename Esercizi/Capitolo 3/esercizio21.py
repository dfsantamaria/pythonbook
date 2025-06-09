# Verificare se il tipo delle variabili definite dall'esercizio 1) è il tipo float. Stampare a schermo il risultato.
float1 = 1.1
float2 = 2.2
float3 = 3.3
float4 = 4.4
float5 = 5.5

tutte_float = True

if not isinstance(float1, float):
    tutte_float = False
if not isinstance(float2, float):
    tutte_float = False
if not isinstance(float3, float):
    tutte_float = False
if not isinstance(float4, float):
    tutte_float = False
if not isinstance(float5, float):
    tutte_float = False

print(tutte_float)
