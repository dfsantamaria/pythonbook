from urllib import request

def esercizio1(url):
    lista = []
    chiavi = []
    resp = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    file = request.urlopen(resp)
    for pos,elemento in enumerate(file):
        if pos == 0:   #leggere l'intestazione
            chiavi = elemento.decode().strip().split(",")
        else: #leggiamo le rimanenti righe
            valori = elemento.decode().strip().split(",")
            dizionario = {}
            for pos_chiavi, chiave in enumerate(chiavi):
                val = valori[pos_chiavi]
                if chiave == "cost" or chiave == "year_built":
                    val = int(val)
                dizionario.update({chiave: val})
                #dizionario[chiavi[pos_chiavi]] = chiave
            lista.append(dizionario)
    return lista


def esercizio2(data):
    total_cost = 0
    for dizionario in data:
        if dizionario["year_built"] == 2010:
            total_cost += dizionario["cost"]
    return total_cost


def esercizio3(data, country):
    architects = []
    for dizionario in data:
        if dizionario["country"] == country:
            if dizionario["architect_designer"] not in architects:
                architects.append(dizionario["architect_designer"])
    return architects

def esercizio4(data):
    buildings = []
    for dizionario in data:
        if dizionario["country"] == "United States of America" and \
                dizionario["city"] != "New York":
            if dizionario["building"] not in buildings:
                buildings.append(dizionario["building"])
    return buildings

def esercizio5(lista, nome_file):
    file = open(nome_file, "w")
    for elemento in lista:
        file.write(str(elemento)+"\n")
    file.write(str(len(lista)))
    file.close()

#prova esercizio1
data = esercizio1("https://pastebin.com/raw/8hgy5yQp")
print("esercizio 1:", data)

#prova esercizio2
total_cost = esercizio2(data)
print("esercizio 2:", total_cost)

#prova esercizio3
architects = esercizio3(data, "United States of America")
print("esercizio 3:", architects)

#prova esercizio4
buildings = esercizio4(data)
print("esercizio 4:", buildings)

#prova esercizio5
esercizio5(buildings,"output.txt")