#Creazione di una lista di dizionari da un CSV

from urllib import request

def crea_dizionari(url:str)->list:
    req = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    lista_diz = []
    intestazione = []
    with  request.urlopen(req) as risposta:
        for pos, riga in enumerate(risposta):
            valori=riga.decode().strip().split(",")
            dizionario = {}
            if pos==0:
                intestazione = valori
            else:
                for pos_elem, elem in enumerate(valori):
                    dizionario.update({intestazione[pos_elem].strip() : elem.strip().replace('\"',"")})
                lista_diz.append(dizionario)
    return lista_diz

lista_diz=crea_dizionari("https://pastebin.com/raw/pNEu1V0K")
print(lista_diz)