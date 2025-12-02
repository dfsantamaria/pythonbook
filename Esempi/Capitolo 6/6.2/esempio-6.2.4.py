# Uso di urllib.request

from urllib import request

url = "https://www.unict.it/"
risposta = request.urlopen(url)
contenuto_binario = risposta.read()
risposta.close()
print(contenuto_binario)  # stampa in  binario
contenuto = contenuto_binario.decode("utf-8")
print(contenuto)  # stampa la decodifica