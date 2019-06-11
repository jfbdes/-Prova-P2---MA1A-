s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
s7=0
s8=0
v= open('series.csv','r')
n= open('series_novas.csv','r')
for line in v.readlines():
    sep= line.split(',')
    if sep[0]=="The Big Bang Theory":
        s1= s1+1
    elif sep[0]=="Friends":
        s2= s2 + 1 
    elif sep[0]=="Breaking Bad":
        s3= s3+1
    elif sep[0]=="Black Mirror":
        s4= s4+1
for line1 in n.readlines():
    sep1= line1.split(',')
    if sep1[0]=="Suits":
        s5= s5+1
    elif sep1[0]=="Fuller House":
        s6= s6+1
    elif sep1[0]=="Designated Survivor":
        s7= s7+1
    elif sep1[0]=="Lucifer":
        s8= s8+1
    
print ('The Big Bang Theory:',s1,'episodios')
print ('Friends:',s2,'episodios')
print ('Breaking Bad:',s3,'episodios')
print ('Black Mirror:',s4,'episodios')
print ('Suits:',s5,'episodios')
print ('Fuller House:',s6,'episodios')
print ('Designated Survivor:',s7,'episodios')
print ('Lucifer:',s8,'episodios')
