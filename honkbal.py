def slag(slagen,bezet=[]):
    punten=0
    erna=[]
    if slagen <= 3:
        if slagen!=0:
            erna.append(slagen)
    else:
        punten += 1
    for getal in bezet:
        plaats=getal+slagen
        if plaats>3:
            punten+=1
        elif plaats!=0:
            erna.append(plaats)
        erna.sort()
        list(set(erna))
    return(punten,erna)
def inning(reeks):
    punt,plaats=0,[]
    punten=0
    for slagen in reeks:
        punt,plaats=slag(slagen,plaats)
        punten+=punt
    return (punten,plaats)









