# Uso di urllib.request

from urllib import request

url = "https://www.google.com/"
risposta = request.urlopen(url)
contenuto_binario = risposta.read()
print(contenuto_binario)  # stampa in codice binario
contenuto = contenuto_binario.decode("utf-8")
print(contenuto)  # stampa la decodifica