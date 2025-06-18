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
            for pos_chiavi, valore in enumerate(valori):
                if chiavi[pos_chiavi]=="roletype":
                    val = valori[pos_chiavi][: valori[pos_chiavi].find("-")].strip()
                else:
                    val = valori[pos_chiavi]
                dizionario.update({chiavi[pos_chiavi]: val})
            lista.append(dizionario)
    return lista

def esercizio2(lista):
    count = 0
    for dizionario in lista:
        if dizionario["race"] == "HISPANIC" and dizionario["sex"]== "FEMALE" and \
            int(dizionario["hiredt"][-2:]) > 17:
            count+=1
    return count

def esercizio3(lista):
    risultato = []
    for dizionario in lista:
        if dizionario["name"] == "SENATE" and dizionario["roletype"]== "URF" and \
            float(dizionario["annual"]) > 1000:
            risultato.append((dizionario["role"], dizionario["lastname"]))
    return  risultato

def esercizio4(lista):
    count = 0
    for dizionario in lista:
        count += float(dizionario["annual"])
    return count / len(lista)


def esercizio5(valore, nome_file):
    file = open(nome_file, "a")
    file.write(str(valore)+"\n")
    file.close()



#prova esercizio1
data = esercizio1("https://pastebin.com/raw/X4fBfzPQ")
print("esercizio 1:", data)

#prova esercizio2
count=esercizio2(data)
print(count)

#prova esercizio3
lista = esercizio3(data)
print(lista)

#prova esercizio4
media = esercizio4(data)
print(media)

#prova esercizio5
esercizio5(media, "output.txt")