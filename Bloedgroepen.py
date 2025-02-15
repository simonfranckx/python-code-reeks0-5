def abo_allelen(bloedgroep):
    allelen_dict= {'A':['A','O'] ,'B':['B','O'], 'AB': ['A','B'] , 'O': ['O'] }
    return allelen_dict[bloedgroep.strip('+-')]
def rhesus_allelen(bloedgroep):
    rhesus_dict = {'+':['+','-'],'-':['-']}
    return rhesus_dict[bloedgroep.strip('ABO')]
def bloedgroep_kind(vader,moeder):
    abo_vader = abo_allelen(vader)
    abo_moeder = abo_allelen(moeder)
    rhesus_vader = rhesus_allelen(vader)
    rhesus_moeder = rhesus_allelen(moeder)
    bloedgroepen=  set()
    bloedgroep_dict = {('A','A'): 'A', ('A','O'):'A', ('B','B'): 'B',('B','O'): 'B', ('A','B'):'AB', ('O','O'): 'O' }
    for allelen_vader in abo_vader:
        for allelen_moeder in abo_moeder:
            combinatie= tuple(sorted([allelen_vader,allelen_moeder]))
            bloedgroepen.add(bloedgroep_dict[combinatie])
    rhesuscombinaties= set()
    rhesus_dict = {('+','-'):'+',('+','+'):'+', ('-','-'):'-'}
    for rhesussen_vader in rhesus_vader:
        for rhesussen_moeder in rhesus_moeder:
            combinatie_rhesus= tuple(sorted([rhesussen_vader,rhesussen_moeder]))
            rhesuscombinaties.add(rhesus_dict[combinatie_rhesus])
    volledige_bloedgroep = []
    for bloedgroep in bloedgroepen:
        for rhesus in rhesuscombinaties:
            volledige_bloedgroep.append(f"{bloedgroep}{rhesus}")
    volledige_bloedgroep.sort()
    return set(volledige_bloedgroep)


def bloedgroep_ouder(ouder, kind):
    bloedgroepen = ['A+','A-','B-','B+','AB+','AB-','O+','O-']
    mogelijke_bloedgroepen = set()
    for bloedgroep in bloedgroepen:
        if kind in bloedgroep_kind(ouder,bloedgroep):
            mogelijke_bloedgroepen.add(bloedgroep)
    return mogelijke_bloedgroepen
