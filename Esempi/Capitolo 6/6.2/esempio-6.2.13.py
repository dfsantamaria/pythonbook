#urllib.request per la lettura di CSV
from urllib import request

def print_lista_csv(url:str):
    req = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with request.urlopen(req) as risposta:
        for pos, riga in enumerate(risposta):
            valori = riga.decode().strip()
            if pos == 0:
                print("L'intestazione è: ", valori)
            else:
                print(f"La riga numero {pos} è: {valori}")

print_lista_csv("https://pastebin.com/raw/pNEu1V0K")