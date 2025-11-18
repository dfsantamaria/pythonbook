# Utilizzo di urllib.request

from urllib import request

url = "https://www.google.com/"
with  request.urlopen(url) as risposta:
    for riga in risposta:
        print(riga.decode())  