# Utilizzo di urllib.request

from urllib import request

url = "https://www.google.com/"
risposta = request.urlopen(url)
for riga in risposta:
    print(riga.decode()) 