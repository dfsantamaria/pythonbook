# Scrivere una funzione che, presa una stringa, stabilisca se questa
# contiene più vocali o consonanti (la stringa può contenere caratteri,
# consonanti, numeri e simboli).
def conta_vocali_consonanti_estesa(s):
    vocali = "aeiouAEIOU"
    consonanti = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    num_vocali = 0
    num_consonanti = 0

    i = 0
    while i < len(s):
        if s[i] in vocali:
            num_vocali = num_vocali + 1
        elif s[i] in consonanti:
            num_consonanti = num_consonanti + 1
        i = i + 1

    if num_vocali > num_consonanti:
        return "più vocali"
    elif num_consonanti > num_vocali:
        return "più consonanti"
    else:
        return "vocali e consonanti in ugual numero"

print(conta_vocali_consonanti_estesa("programmazione123!"))
