lista=[]
lista2=[]
x= open('series.csv', 'r')
y= open('series_novas.csv', 'r')
for line in x.readlines():
    separado = line.split(',')
    lista.append(separado)

for line in y.readlines():
    ss = line.split(',')
    lista2.append(ss)


print(lista)
print(lista2)
        


