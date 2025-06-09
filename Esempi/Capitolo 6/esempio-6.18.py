# urllib.request e scrittura su file

from urllib import request

url = "https://www.google.com/"
risposta = request.urlopen(url)
contenuto_binario = risposta.read()
contenuto = contenuto_binario.decode("utf-8")
with  open("pagina.txt", "w") as f:
    f.write(contenuto)