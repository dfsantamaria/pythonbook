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
        else:
             elemento = elemento.split(",\"")[0]
             valori = elemento.split(",")
             dizionario = {}
             for pos_chiavi, valore in enumerate(valori):
                 dizionario.update({chiavi[pos_chiavi]: valore})
             lista.append((pos,dizionario))
    return lista


def esercizio2(lista):
    newlist = []
    for elemento in lista:
        newdict = elemento[1].copy()
        newdict.pop("asin")
        newlist.append((elemento[0], newdict))
    return newlist


def esercizio3(lista):
    count = 0
    for elemento in lista:
        if len(elemento[1].get("price"))>0:
           count += float(elemento[1].get("price"))
    return count

def esercizio4(nome_file, lista):
    file = open(nome_file, "w")
    for elemento in lista:
        file.write(str(elemento[0]) +"-" + elemento[1].get("asin")+ "-" +
                   elemento[1].get("brand")+ "-"+ elemento[1].get("price")+"\n")
    file.close()

def esercizio5(nome_file):
    file = open(nome_file, "r")
    for elemento in file:
        print(elemento.strip())
    file.close()

#prova esercizio 1
data = esercizio1("https://pastebin.com/raw/qDwi4aj8")
print(data)

#prova esercizio 2
data2 = esercizio2(data)
print(data2)

#prova esercizi 3
print(esercizio3(data2))

#prova esercizio 4
miofile="output.txt"
esercizio4(miofile, data)

#prova esercizio 5
esercizio5(miofile)