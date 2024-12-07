


def cijferfrequentie(string):
    getallen = '0123456789'
    frequentie = ()
    for cijfer in getallen:
        hoeveel = string.count(cijfer)
        frequentie+=(hoeveel,)
    return frequentie

def beschrijving(string):
    beschreven=''
    index=0
    for getal in string:
        combinatie=(str(getal)+str(index)).lstrip('0')
        if combinatie=='':
            combinatie='0'
        beschreven+=combinatie+' '
        index+=1
    beschreven=beschreven.rstrip(' ')
    return beschreven

def iszelfbeschrijvend(reeks):
    i=0
    reeks=list(reeks)
    if len(reeks)==1:
        i=1
    for string in reeks:
        volledige_beschr=beschrijving(cijferfrequentie(str((reeks[:i+1]))))
        if string!= volledige_beschr:
            return False
        i+=1
    return True
print(iszelfbeschrijvend(['F1gur471v3ly 5p34k1ng?']))
def iszelfbeschrijvend_2(*reeks):
    i=0
    if len(reeks)==1:
        i=1
    for string in reeks:
        volledige_beschr = beschrijving(cijferfrequentie(str(reeks[:i + 1])))
        if string != volledige_beschr:
            return False
        i += 1
    return True



