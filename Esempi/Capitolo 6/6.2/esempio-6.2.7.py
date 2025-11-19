from urllib import request

url = "https://www.unict.it/"
req = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with  request.urlopen(req) as risposta:
   for riga in risposta:
        print(riga.decode())   