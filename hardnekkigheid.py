#vermenigvuldiging


def vermenigvuldiging(n):
    product=1
    n=str(n)
    for getal in n:
        cijfer=int(getal)
        product*=cijfer
    return product

#digitale wortel

def digitale_wortel(invoer_wortel):
    invoer_wortel=str(invoer_wortel)
    while len(invoer_wortel)>1:
        uitkomst=vermenigvuldiging(invoer_wortel)
        invoer_wortel=str(uitkomst)
    return int(invoer_wortel)


#hardnekkigheid

def hardnekkigheid(invoer_hardnekkigheid):
    stappen=0
    invoer_hardnekkigheid=str(invoer_hardnekkigheid)
    while len(invoer_hardnekkigheid)>1:
        uitkomst=vermenigvuldiging(invoer_hardnekkigheid)
        invoer_hardnekkigheid=str(uitkomst)
        stappen+=1
    return stappen

#hardnekkigste

def hardnekkigste(a,b):
    max_hardnekkigheid=0
    cijfer=a
    for getal in range(a,b+1):
        huidige_hardnekkigheid=hardnekkigheid(str(getal))
        if huidige_hardnekkigheid>max_hardnekkigheid:
            max_hardnekkigheid=huidige_hardnekkigheid
            cijfer=getal
    return cijfer








