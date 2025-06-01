from urllib import request

def esercizio1(url):
    lista = []
    chiavi = []
    file = request.urlopen(url)
    for pos,elemento in enumerate(file):
        elemento=elemento.decode().strip()
        if pos == 0:   #leggere l'intestazione
            chiavi = elemento.split(",")
        else:             
             valori = elemento.split(",")
             dizionario = {}
             for pos_chiavi, valore in enumerate(valori):
                 if  "Ingredienti" in chiavi[pos_chiavi]:
                     valore= valore.split("-")
                 elif "Tempo" in chiavi[pos_chiavi] or "Calorie" in chiavi[pos_chiavi]:
                     valore=int(valore)
                 dizionario.update({chiavi[pos_chiavi]: valore})
             lista.append(dizionario)
    return lista


def esercizio2(lista):
    calorie = 0
    for elemento in lista:
        calorie += int(elemento["Calorie"])
    return calorie

def esercizio3(lista):
    nuovalista = []
    for  elemento in lista:
        if "Uova" not in elemento["Ingredienti Primari"] and "Uova" not in elemento["Ingredienti Secondari"]:
            nuovalista.append(elemento)
    return nuovalista


def esercizio4(lista, calorie, ingr, tempo):
    nuovalista = []
    for elemento in lista:
        if elemento["Calorie"] <= calorie and ingr not in elemento["Ingredienti Primari"] and \
                ingr not in elemento["Ingredienti Secondari"] and  elemento["Tempo"] <= tempo:
           nuovalista.append((elemento["Nome"], elemento["Calorie"],elemento["Tempo"]))
    return nuovalista

def esercizio5(nome_file, data):
    file = open(nome_file, "w")
    for elemento in data:
        for pos, elem in enumerate(elemento):
           file.write(str(elem))
           if(pos!=len(elemento)-1):
               file.write(" - ")
           else:
               file.write(" ; ")
        file.write("\n")
    file.close()

#prova esercizio 1
data = esercizio1("https://pastebin.com/raw/b9qDVyzE")
print(data)

#prova esercizio 2
print(esercizio2(data))

#prova esercizio 3
newdata=esercizio3(data)
print(newdata)

#prova esercizio 4
lista = esercizio4(data, 700, "Timo", 50)
print(lista)

#prova esercizio 5
esercizio5("esame260624", lista)