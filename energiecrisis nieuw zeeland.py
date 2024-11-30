def noodplan(aantal_gebieden,sprong):
    lijst=list(range(1,aantal_gebieden+1))
    index = 0
    nieuwe_lijst=[1]
    while len(nieuwe_lijst)<aantal_gebieden:
        count= 0
        while count<sprong:
            index=(index+1)%aantal_gebieden
            if lijst[index] not in nieuwe_lijst:
                count+=1
        nieuwe_lijst.append(lijst[index])

    return nieuwe_lijst

def geldige_sprong(aantal_gebieden):
    sprong=1

    while True:
        resultaat=noodplan(aantal_gebieden,sprong)
        if resultaat[-1]==13:
            return sprong
        if sprong>=aantal_gebieden:
            return None
        sprong+=1











