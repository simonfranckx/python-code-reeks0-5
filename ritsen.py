def samenvoegen(lijst1,lijst2):
    kleinste=min([len(lijst1),len(lijst2)])
    samengevoegd=[]
    for i in range(0,kleinste):
        samengevoegd.append(lijst1[i])
        samengevoegd.append(lijst2[i])
    return samengevoegd
def weven(lijst1,lijst2):
    grootste = max([len(lijst1), len(lijst2)])
    samengevoegd = []
    for i in range(0, grootste):
        plaats1=i%len(lijst1)
        samengevoegd.append(lijst1[plaats1])
        plaats2=i%len(lijst2)
        samengevoegd.append(lijst2[plaats2])
    return samengevoegd
def ritsen(lijst1,lijst2):
    geritst=samenvoegen(lijst1,lijst2)
    kleinste = min([len(lijst1), len(lijst2)])
    if len(lijst1)>len(lijst2):
        geritst+=lijst1[kleinste:]
    else:
        geritst+=lijst2[kleinste:]
    return geritst
