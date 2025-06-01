from urllib import request

def esercizio1(url):
    result =[]
    file = request.urlopen(url)
    header=[]
    row_number = 1
    for pos,line in enumerate(file):
        if pos==0:
           header= line.decode().strip().split(",")
        else:
           sub_list =[]
           row =  line.decode().strip().split(",")
           for cell_pos, cell in enumerate(row):
               sub_list.append( (header[cell_pos], row_number, cell))
           row_number += 1
           result.append(sub_list)
    return result


data = esercizio1("https://pastebin.com/raw/tnLxFxJs")
#prova esercizio1
for element in data:
    print(element)

def esercizio2(lista):
    result = []
    for elemento in lista:
        if elemento[2][2] not in result:
            result.append(elemento[2][2])
    return result


#prova esercizio2
es2= esercizio2(data)
print(es2)


def esercizio3(lista):
    result = []
    for element in lista:
        if int(element[1][2]) > 2017:
           result.append(element[0][2])
    return result

#prova esercizio3
es3 = esercizio3(data)
print(es3)

def esercizio4(lista):
    result = []
    for element in lista:
        if int(element[4][2]) > int(element[5][2]):
            result.append(element[0][2])
    return result


#prova esercizio4
es4 = esercizio4(data)
print(es4)

def esercizio5(val1, val2, val3):
    file = open("output.txt", "w")
    file.write(str(val1)+"\n")
    file.write(str(val2)+"\n")
    file.write(str(val3)+"\n")
    file.close()

#prova esercizio5
esercizio5(es2,es3, es4)