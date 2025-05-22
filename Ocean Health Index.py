def gemiddelde(lijst):
    nieuwe_lijst=[]
    for getal in lijst:
        if getal is not None:
            nieuwe_lijst.append(getal)
    if not nieuwe_lijst:
        return None
    else:
        return sum(nieuwe_lijst)/len(nieuwe_lijst)
def gegevensbank(tekstbestand):
    d = {}
    with open(tekstbestand,'r') as bestand:
        for line in bestand:
            omgezet= line.strip('\n').split('\t')
            for index,getallen in enumerate(omgezet[2:]):
                if getallen == '':
                    omgezet[index+2]=None
                else:
                    omgezet[index+2]= int(getallen)
                d[omgezet[1]]=omgezet[2:]
    return d

def oceanHealthIndex(kuststaat, dic):





