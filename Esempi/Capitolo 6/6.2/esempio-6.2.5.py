# Utilizzo di urllib.request

from urllib import request

url = "https://www.unict.it/"
risposta = request.urlopen(url)
for riga in risposta:
    print(riga.decode())
risposta.close()