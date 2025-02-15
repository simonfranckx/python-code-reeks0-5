alfabet="abcdefghijklmnoöpqrstuvwxyz"
ALFABET=alfabet.upper()
def isgeldig(symbool,naam,lengte=None):
    if lengte is not None:
        if len(symbool) != lengte:
            return False
    if symbool[0] not in ALFABET:
        return False
    if len(symbool)>1:
        for letter in symbool[1:]:
            if letter not in alfabet:
                return False
    plaats=-1
    for letter in symbool.lower():
        nieuwe_plaats= naam.lower().find(letter,plaats+1)
        if nieuwe_plaats <= plaats  or nieuwe_plaats == -1:
            return False
        plaats=nieuwe_plaats
    return True
def symbolen(naam):
    uitkomstenlijst = set()

    for letter in naam:
        for andere_letter in naam:
            uitkomsten = str(letter + andere_letter)
            uitkomsten= uitkomsten.capitalize()
            if isgeldig(uitkomsten, naam,2):
                uitkomstenlijst.add(uitkomsten)
    return uitkomstenlijst

def voorkeur(naam,laatste=False):
    combinaties = symbolen(naam)
    if laatste is True:
        return max(combinaties)
    return min(combinaties)



