def serienummer(nummers):
    assert ( isinstance(nummers,str) and nummers.isdigit() and int(nummers)!=0 or isinstance(nummers,int) and nummers>0) , "ongeldig serienummer"
    nummers=str(nummers)
    while len(nummers)<8:
        nummers=f'0{nummers}'
    return nummers
def standvastig(nummers):
    serie=serienummer(nummers)
    for nummer in serie:
        if nummer!=serie[0]:
            return False
    return True
def radar(nummers):
    serie=serienummer(nummers)
    if standvastig(serie):
        return False

    serie=list(serie)
    omgekeerd=serie[::-1]

    if omgekeerd==serie:
        return True
    return False
def repeater(nummers):
    serie=serienummer(nummers)
    if standvastig(serie):
        return False
    helft=int(len(serie))//2
    if serie[:helft]==serie[helft:]:
        return True
    return False
def radarrepeater(nummers):
    if repeater(nummers) and radar(nummers):
        return True
    return False
def numismatist(reeks,soort=standvastig):
    lijst=[]
    for serie in reeks:
        if soort(serie):
            lijst.append(serie)
    return lijst

