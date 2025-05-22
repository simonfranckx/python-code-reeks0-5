def massatabel(locatie_tekstbestand):
    tabel={}
    with open(locatie_tekstbestand,'r') as tekstbestand:
        for line in tekstbestand:
            hoofdletter, cijfer= line.split()
            tabel[hoofdletter] = float(cijfer)
    return tabel

def eiwitmassa(eiwitsequentie,tabel,peptide=False):
    molecuulmassa=float(18.01056)
    if peptide is True:
        molecuulmassa= 0
    for letter in eiwitsequentie:
        molecuulmassa+=tabel[letter]
    return molecuulmassa