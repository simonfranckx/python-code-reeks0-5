polymeer=input('Geef een polymeer: ')
n=0
while n+1<len(polymeer):
    positie1= n
    positie2=n+1
    letter1=polymeer[positie1]
    letter2=polymeer[positie2]
    if letter1.lower()==letter2.lower() and letter1!=letter2:
        stuk1=polymeer[0:positie1]
        stuk2=polymeer[positie2+1:]
        polymeer=stuk1+stuk2
        if n>0:
            n-=1
    else:
        n+=1
lengte=len(polymeer)
print(f"{polymeer}({lengte})")
