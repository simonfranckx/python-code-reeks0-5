def isstijgend(reeks):
    n=0
    while n<len(reeks)-1:
        if reeks[n]>reeks[n+1]:
            return False
        n+=1
    return True
def frequentiereeks(reeks):
    assert isstijgend(reeks), "gegeven reeks is niet stijgend"
    nieuwe_reeks=[]

    for getal in list(range(1,reeks[-1]+2)):
        hoeveel=0
        i=0
        while reeks[i]<getal:
            hoeveel+=1
            if i<len(reeks)-1:
                i+=1
            else:
                break
        nieuwe_reeks.append(hoeveel)
    return nieuwe_reeks
def verhogen(reeks):
    reeks=list(reeks)
    for plaats,getal in enumerate(reeks):
        verhoogd=getal+plaats+1
        reeks[plaats]=verhoogd
    return reeks


def complementaire_reeksen(reeks):
    verhoogde_frequentie=verhogen(frequentiereeks(reeks))
    return (verhogen(reeks),verhoogde_frequentie)
