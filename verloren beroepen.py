


def volgende_letter(v,w):
    v=v.upper()
    w=w.upper()
    if v in w and w.count(v)==1:
        plaats=w.find(v)
        if plaats+len(v)<len(w):
            return w[plaats+len(v)]
    return ''

def uitbreiden(p,woordenlijst):
    verborgen=p.upper()
    for woord in woordenlijst:
        p=p[1:]
        volgend=volgende_letter(p,woord)
        if volgend != '':
            p+=volgend
            verborgen+=volgend

        else:
            return ''
    return verborgen


def beroep(woordenlijst,lengte=2):
    eerste_woord=woordenlijst[0]
    for index in range(0,len(eerste_woord)-lengte+1):
        n_gram= eerste_woord[index:index+lengte]
        verborgen=uitbreiden(n_gram,woordenlijst[1:])
        if verborgen!='':
            return verborgen
    return ''
