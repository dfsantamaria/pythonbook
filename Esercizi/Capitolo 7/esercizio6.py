# Scrivere una funzione che, presa una stringa, stabilisca se questa con-
# tiene più vocali o consonanti (la stringa può contenere solo caratteri
# o consonanti).
def conta_vocali_consonanti(s):
    vocali = "aeiouAEIOU"
    num_vocali = 0
    num_consonanti = 0

    i = 0
    while i < len(s):
        if s[i] in vocali:
            num_vocali = num_vocali + 1
        else:
            num_consonanti = num_consonanti + 1
        i = i + 1

    if num_vocali > num_consonanti:
        return "più vocali"
    elif num_consonanti > num_vocali:
        return "più consonanti"
    else:
        return "vocali e consonanti in ugual numero"

print(conta_vocali_consonanti("programmazione"))

