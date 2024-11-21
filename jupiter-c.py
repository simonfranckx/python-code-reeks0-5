def reduceer(codewoord):
    woord=''
    for letter in codewoord:
        if letter not in woord:
            woord+=letter
    return woord
def codeer(serienummer, codewoord):
    woord=reduceer(codewoord)
    assert len(woord)==10, 'ongeldig codewoord'
    voor_lijst=woord[-1]+woord[:10]
    serienummer=str(serienummer)
    gecodeerd=''
    for cijfer in serienummer:
        gecodeerd+=voor_lijst[int(cijfer)]
    return gecodeerd
def decodeer(gecodeerd,codewoord):
    woord = reduceer(codewoord)
    assert len(woord) == 10, 'ongeldig codewoord'
    voor_lijst = woord[-1] + woord[:10]
    serienummer=''
    for letter in gecodeerd:
        serienummer+=str(voor_lijst.find(letter))
    return int(serienummer)
def volgende(gecodeerd,codewoord):
    woord = reduceer(codewoord)
    assert len(woord) == 10, 'ongeldig codewoord'
    serienummer=decodeer(gecodeerd,codewoord)
    serienummer=serienummer+1
    nieuw_gecodeerd=codeer(serienummer,codewoord)
    return nieuw_gecodeerd



