from urllib import request

def esercizio_1(url):
    lista = []
    chiavi = []
    resp = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    file = request.urlopen(resp)
    for pos,elemento in enumerate(file):
        elemento=elemento.decode().strip()
        if pos == 0:   #leggere l'intestazione
            chiavi = elemento.split(",")
        else:
             dizionario = {}
             for pos_chiavi, linea in enumerate(elemento.split(",")):
                 if chiavi[pos_chiavi] == "Quantità":
                    dizionario.update({chiavi[pos_chiavi]:int(linea)})
                 elif chiavi[pos_chiavi] in ["Prezzo Unitario", "Totale"]:
                    dizionario.update({chiavi[pos_chiavi]:float(linea)})
                 else:
                     dizionario.update({chiavi[pos_chiavi]:linea})
             lista.append(dizionario)
    return lista


def esercizio_2(lista):
    max = [None,0]
    for elem in lista:
        if elem["Totale"] > max[1]:
            max = [elem["ID Ordine"], elem["Totale"]]
    return max


def esercizio_3(lista):
    contatore = 0
    for elem in lista:
        if elem["Prodotto"] == "Smartphone":
            contatore += 1
    return contatore

def esercizio_4(lista):
    elenco = []
    for elem in lista:
        totale_corretto = elem["Quantità"]*elem["Prezzo Unitario"]
        if elem["Totale"] != totale_corretto:
            elenco.append((elem["ID Ordine"], totale_corretto, elem["Totale"]))
    return elenco



def esercizio_5(lista, nome_file):
    file = open(nome_file, "w")
    for elem in lista:
        file.write(elem[0] + " ," + str(elem[1]) + " ," + str(elem[2]) + ";\n")
    file.close()

data = esercizio_1("https://pastebin.com/raw/90J6YpK6")
print(data)

print(esercizio_2(data))
print(esercizio_3(data))
towrite = esercizio_4(data)
print(towrite)
print(esercizio_5(towrite, "esame.txt"))

