#Liste per la memorizzazione dei valori di un CSV
from urllib import request

def print_lista_csv(url:str):
    req = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with request.urlopen(req) as risposta:
        for pos, riga in enumerate(risposta):
            valori = riga.decode().strip().split(",")
            if pos == 0:
               print("L'intestazione contiene i valori: ", valori)
            else:
               print(f"La riga numero {pos} contiene i valori: {valori}")

print_lista_csv("https://pastebin.com/raw/pNEu1V0K")