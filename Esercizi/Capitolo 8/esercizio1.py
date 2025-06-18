from urllib import request

def esercizio1(url):
    result =[]
    resp = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})    
    file = request.urlopen(resp)
    header=[]
    for pos,line in enumerate(file):
        if pos==0:
           header= line.decode().strip().split(",")
        else:
           sub_list =[]
           row =  line.decode().strip().split(",")
           for cell_pos, cell in enumerate(row):
               sub_list.append( (header[cell_pos], cell_pos, cell) )
           result.append(sub_list)
    return result


data = esercizio1("https://pastebin.com/raw/RtwHi7yN")
#prova esercizio1
for element in data:
    print(element)

def esercizio2(lista):
    result = []
    for element in lista:
        date = element[2][2].strip()
        if "-" in date:
            date = date.split("-")[0]
        elif "s" in date:
            date = date.replace("s","")
        if int(date) < 1960:
           result.append(element[0][2])
    return result

#prova esercizio2
print(esercizio2(data))


def esercizio3(lista):
    result = []
    for element in lista:
        author = element[1][2].strip()
        if author == '':
            result.append(element[0][2])
    return result

#prova esercizio3
print(esercizio3(data))


def esercizio4(lista):
    result = []
    for element in lista:
        price=element[4][2].strip().replace("$","").replace(".","")
        if int(price) >= 1000000:
            result.append(element[1][2])
    return result


#prova esercizio4
print(esercizio4(data))

def esercizio5(lista, nome_file):
    file = open(nome_file, "w")
    for line in lista:
            file.write(str(line) + "\n")
    file.close()

#prova esercizio5
esercizio5(data,"test.txt")