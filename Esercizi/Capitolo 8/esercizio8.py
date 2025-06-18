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
                 if chiavi[pos_chiavi] in ["Publication Year", "Earnings (EUR)"]:
                    dizionario.update({chiavi[pos_chiavi]:int(linea)})
                 elif chiavi[pos_chiavi] == "Rating":
                    dizionario.update({chiavi[pos_chiavi]:float(linea)})
                 else:
                     dizionario.update({chiavi[pos_chiavi]:linea})
             lista.append(dizionario)
    return lista


def esercizio_2(lista):
    films = []
    for elem in lista:
        if elem["Rating"] > 9.0:
            films.append(elem["Title"])
    return films


def esercizio_3(lista, anno):
    films = []
    for elem in lista:
        if elem["Publication Year"] == anno:
            films.append((elem["Title"], elem["Director"]))
    return  films


def verifica_anno(lista, anno):
    for pos, elem in enumerate(lista):
        if elem[0] == anno:
            return pos
    return -1

def esercizio_4(lista):
    films = []
    for elem in lista:
        pos = verifica_anno(films, elem["Publication Year"] )
        if pos >= 0:
           films[pos] = (films[pos][0], films[pos][1]+elem["Earnings (EUR)"], films[pos][2] + [elem["Title"]])
        else:
            films.append((elem["Publication Year"], elem["Earnings (EUR)"], [elem["Title"]]))
    return films


def esercizio_5(lista, nome):
    file = open(nome, "w")
    for elem in lista:
        file.write(str(elem[0])+", "+str(elem[1])+":")
        for pos, film in enumerate(elem[2]):
            file.write(film)
            if pos == len(elem[2]) - 1:
               file.write(";")
            else:
                file.write(",")
        file.write("\n")
    file.close()


data = esercizio_1("https://pastebin.com/raw/NkMtkZEZ")
print(data)

print(esercizio_2(data))

print(esercizio_3(data, 1994))

films = esercizio_4(data)
print(films)

esercizio_5(films, "esame.txt")
