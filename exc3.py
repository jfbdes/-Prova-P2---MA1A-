"""
Professor nesse eu só adicionei o narcos ok? que eu tinha esquecido de resto tudo deu certo!
"""
s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
s7=0
s8=0
s9=0
v= open('series.csv','r')
for line in v.readlines():
    s= line.split(',')
    if s[0]=="The Big Bang Theory":
        s1= s1+1
    elif s[0]=="Friends":
        s2= s2 + 1 
    elif s[0]=="Breaking Bad":
        s3= s3+1
    elif s[0]=="Black Mirror":
        s4= s4+1
n= open('series_novas.csv','r')
for line1 in n.readlines():
    sn= line1.split(',')
    if sn[0]=="Suits":
        s5= s5+1
    elif sn[0]=="Fuller House":
        s6= s6+1
    elif sn[0]=="Designated Survivor":
        s7= s7+1
    elif sn[0]=="Lucifer":
        s8= s8+1
    elif sn[0] == "Narcos":
        s9 = s9 +1
    
print ('The Big Bang Theory:',s1,'episódios')
print ('Friends:',s2,'episódios')
print ('Breaking Bad:',s3,'episódios')
print ('Black Mirror:',s4,'episódios')
print ('Suits:',s5,'episódios')
print ('Fuller House:',s6,'episódios')
print ('Designated Survivor:',s7,'episódios')
print ('Lucifer:',s8,'episódios')
print ('Narcos:',s9,'episódios')
