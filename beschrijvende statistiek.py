import math
def gemiddelde(steekproef):
    som=0
    n=len(steekproef)
    for getal in steekproef:
        som+=getal
    gemiddeld=som/n
    return gemiddeld
def mediaan(steekproef):
    steekproef.sort()
    n=len(steekproef)
    if n%2==1:
        middel=int(n/2)
        return steekproef[middel]

    middel1=int((n-1)/2)
    medi=(steekproef[middel1]+steekproef[middel1+1])/2
    return medi


def standaardafwijking(steekproef):
    n=len(steekproef)
    som=0
    gem=gemiddelde(steekproef)
    for getal in steekproef:
        verschil=(getal-gem)**2
        som+=verschil
    sa=math.sqrt((1/(n-1))*som)
    return sa
