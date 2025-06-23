from urllib import request

def esercizio1(url):
    lista = []
    chiavi = []
    req = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    file = request.urlopen(req)
    for pos,elemento in enumerate(file):
        elemento=elemento.decode().strip()
        if pos == 0:   #leggere l'intestazione
            chiavi = elemento.split(",")
            for indice, chiave in enumerate(chiavi):
                chiavi[indice] = chiave.strip().replace('"','')
        else:
            valori = elemento.split(",")
            for indice, valore in enumerate(valori):
               valori[indice] = valore.strip().replace('"','')
            dizionario = {}
            for pos_chiavi, valore in enumerate(valori):
                if chiavi[pos_chiavi] == "Anno" or chiavi[pos_chiavi]=="ID":
                    dizionario.update({chiavi[pos_chiavi]: int(valore)})
                else:
                    dizionario.update({chiavi[pos_chiavi]: valore})
            lista.append(dizionario)
    return lista

def esercizio2(lista):
    ids = []
    for elemento in lista:
        if elemento["Anno"]>=1500 and elemento["Anno"]<=1600:
            ids.append(elemento["ID"])
    return ids

def esercizio3(id, lista):
    tuples = []
    for diz in lista:
        if diz["ID"] == id:
            for elemento in diz:
                tuples.append((elemento, diz[elemento]))
            break
    return tuples

def trovaMuseo(museo, musei):
    for pos, elem in enumerate(musei):
        if museo == elem[0]:
           return pos
    return -1

def esercizio4(lista):
    musei = []
    for elemento in lista:
        trova = trovaMuseo(elemento["Museo"], musei)
        if trova == -1:
            musei.append((elemento["Museo"], [elemento["Titolo"]]))
        else:
            musei[trova][1].append(elemento["Titolo"])
    return musei

def esercizio5(nome_file, data):
    file = open(nome_file, "w")
    for riga in data:
        file.write(riga[0]+" : ")
        for pos, elem in enumerate(riga[1]):
           file.write(str(elem))
           if(pos!=len(riga[1])-1):
               file.write(", ")
           else:
               file.write(";")
        file.write("\n")
    file.close()


#prova esercizio 1
data = esercizio1("https://pastebin.com/raw/pNEu1V0K")
print(data)

#prova esercizio 2
ids = esercizio2(data)
print(ids)

#prova esercizio 3
tuples = esercizio3(3, data)
print(tuples)

#prova esercizio 4
opere = esercizio4(data)
print(opere)

#prova esercizio 5
esercizio5("esame120724.txt", opere)