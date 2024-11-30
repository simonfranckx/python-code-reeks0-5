def volgende(reeks_getallen):
    laatste=abs(reeks_getallen[-1]-reeks_getallen[0])
    ducci=()
    for index,getal in enumerate(reeks_getallen[:-1]):
        nieuw=abs(reeks_getallen[index]-reeks_getallen[index+1])
        ducci+=(nieuw,)
    ducci+=(laatste,)
    return ducci

def ducci(reeks_getallen):

    reeks=tuple(reeks_getallen)
    geheel=(reeks,)
    if sum(reeks)==0:
        return geheel
    while True:
        nieuwe_reeks= volgende(reeks)

        if nieuwe_reeks in geheel:
            geheel+=(nieuwe_reeks,)
            break
        geheel+=(nieuwe_reeks,)
        if sum(nieuwe_reeks)==0:
            break
        reeks=nieuwe_reeks
    return geheel
def periode(reeks_getallen):
    reeks = tuple(reeks_getallen)
    geheel = (reeks,)
    if sum(reeks)==0:
        return 0
    teller=0
    while True:
        nieuwe_reeks = volgende(reeks)

        if nieuwe_reeks in geheel:
            teller+=1
            plaats=geheel.index(nieuwe_reeks)
            teller=teller-plaats
            geheel += (nieuwe_reeks,)
            break
        geheel += (nieuwe_reeks,)
        teller+=1
        if sum(nieuwe_reeks) == 0:
            return 0
        reeks = nieuwe_reeks
    return teller

