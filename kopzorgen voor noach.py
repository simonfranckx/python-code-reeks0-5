def splitsing(w):
    klinkers='aoiue'
    klinkers_hoofdletter='AOIUE'
    plaats=0
    index=0
    while w[index] not in klinkers and w[index] not in klinkers_hoofdletter :
        plaats+=1
        index+=1
    prefix=w[:plaats]
    suffix=w[plaats:]
    return prefix, suffix



def kruising(w1,w2):

    prefix1, suffix1=splitsing(w1)
    prefix2, suffix2=splitsing(w2)
    woord1=prefix1+suffix2
    woord2=prefix2+suffix1

    return woord1, woord2



