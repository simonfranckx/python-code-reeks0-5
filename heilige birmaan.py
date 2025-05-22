def kleur(genotype):
    d = {}
    for k in ['CCDD', 'CCDd', 'CCdD', 'CcDD', 'CcDd', 'CcdD', 'cCDD', 'cCDd', 'cCdD']:
        d[k] = 'seal'
    for k in ['ccDD', 'ccDd', 'ccdD']:
        d[k] = 'chocolate'
    for k in ['CCdd', 'Ccdd', 'cCdd']:
        d[k] = 'blue'
    for k in ['ccdd']:
        d[k] = 'lilac'
    return d[genotype]
def combinaties(genotype):
    lijst= []
    for gen1 in genotype[0:2]:
        for gen2 in genotype[2:4]:
            combinatie =gen1+gen2
            lijst.append(combinatie)
    return lijst

def punnett(kater,kattin,pprint=False):
    if pprint:
        punet = ''
        aantal_kind= 0
        for combinatie in  combinaties(kater):
            for combinatiev in combinaties(kattin):
                kind= combinatie[0]+ combinatiev[0]+ combinatie[1]+ combinatiev[1]
                aantal_kind+=1
                if aantal_kind==16:
                    punet+= ' '+kind
                elif aantal_kind%4==0:
                    punet+=' ' + kind +'\n'
                elif aantal_kind%4==1:
                    punet+= kind
                else:
                    punet+= ' '+ kind
        return punet
    else:
        punet = []
        for combinatie in combinaties(kater):
            nieuwe_lijst = []
            for combinatiev in combinaties(kattin):
                kind = combinatie[0] + combinatiev[0] + combinatie[1] + combinatiev[1]
                nieuwe_lijst.append(kind)
            punet.append(nieuwe_lijst)
        return punet
def kleurverdeling(kat, kattin):
    code= punnett(kat, kattin)
    d={}
    for comb_list in code:
        for comb in comb_list:
            kleurtje= kleur(comb)
            if kleurtje in d:
                d[kleurtje]= d[kleurtje]+1
            else:
                d[kleurtje]=1
    return d





