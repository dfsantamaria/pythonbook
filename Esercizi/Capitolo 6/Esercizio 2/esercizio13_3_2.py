# Stampare a schermo gli id delle variabili definite dall'esercizio 1).
# Riscrivere gli esercizi precedenti usando una funzione da includere in un modulo.

def stampa_id_float():
    float1 = 1.1
    float2 = 2.2
    float3 = 3.3
    float4 = 4.4
    float5 = 5.5
    print(id(float1), id(float2), id(float3), id(float4), id(float5))
