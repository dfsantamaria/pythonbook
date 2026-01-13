from urllib import request

#esercizio 1
def esercizio1(url):
    risultato=[]
    chiavi=[]
    with request.urlopen(url) as oggetto:
        for pos, riga in enumerate(oggetto):
            if pos==0:
                chiavi=riga.strip().decode().split(",")
                for posC, chiave in enumerate (chiavi):
                    chiavi[posC]= chiave.strip()
            else:
                valori=riga.strip().decode().split(",")
                diz={}
                for posV, valore in enumerate (valori):
                    valori[posV]=valore.replace('"','').strip()
                    if chiavi[posV] in ["Anno", "ID"]:
                        valori[posV]= int(valori[posV])
                    diz.update({chiavi[posV]: valori[posV]})
                risultato.append(diz)
        return risultato


#esercizio 2
def esercizio2 (lista:list)-> list:
    risultato=[]
    for diz in lista:
        if diz["Città"] == "Parigi":
            risultato.append(diz["ID"])
    return risultato



#esercizio 3
def esercizio3 (nome:str, lista:list)-> list:
    risultato=[]
    for diz in lista:
        if nome in diz["Titolo"]:
            risultato.append(diz["Titolo"])
    return risultato



#esercizio 4
def contiene_tupla_citta(lista:list, stringa:str) ->int:
    for pos, elemento in enumerate(lista):
        if elemento[0] == stringa:
            return pos
    return -1


def esercizio4 (lista:list) -> list:
    risultato=[]
    for diz in lista: #seleziono città e la appendo alla lista delle città.
       if (pos := contiene_tupla_citta(risultato, diz["Città"]) >= 0 ):
           risultato[pos] = (risultato[pos][0],risultato[pos][1]+[diz["Titolo"]])
       else:
           risultato.append((diz["Città"], [diz["Titolo"]]))
    return risultato



#esercizio 5
def esercizio5(lista:list,nome:str):
    with open(nome,"w", encoding="utf-8") as file:
        for tupla in lista:
            file.write(f"{tupla[0]}: ")
            titoli= tupla[1]
            for pos, titolo in enumerate (titoli):
                file.write(f"{titolo}")
                if pos < len(titoli)-1:
                    file.write(", ")
                else:
                    file.write(";\n")



lista_diz= esercizio1("https://pastebin.com/raw/pNEu1V0K")
print(lista_diz)
opere_Parigi=esercizio2(lista_diz)
print(opere_Parigi)
titoli_filtrati=esercizio3("La", lista_diz)
print(titoli_filtrati)
tuple_citta_opere=esercizio4(lista_diz)
print(tuple_citta_opere)
esercizio5(tuple_citta_opere, "città e opere.txt")