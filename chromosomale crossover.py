def crossoverpunten(chrom1,chrom2):
    overeenkomstig=0
    i=0
    j=0
    i_crossover=0
    j_crossover=0
    som=0
    while i<len(chrom1) and j<len(chrom2):
        getal1=chrom1[i]
        getal2=chrom2[j]
        if getal1<getal2:
            i+=1
        elif getal1==getal2:
            overeenkomstig+=1
            pad=max(sum(chrom1[i_crossover:i+1]),sum(chrom2[j_crossover:j+1]))
            som+=pad
            i+=1
            j+=1
        else:
            j+=1
    return overeenkomstig

def maximaleSom(chrom1,chrom2):
    overeenkomstig=0
    i=0
    j=0
    i_crossover=-1     #vormt 0 bij begin, later aangepast naar juiste waarde in loop
    j_crossover=-1
    som=0
    while i<len(chrom1) and j<len(chrom2):
        getal1=chrom1[i]
        getal2=chrom2[j]
        if getal1<getal2:
            i+=1
        elif getal1==getal2:
            overeenkomstig+=1
            pad=max(sum(chrom1[i_crossover+1:i+1]),sum(chrom2[j_crossover+1:j+1])) #max tussen elk crossoverpunt, met einde inclusief
            som+=pad
            i_crossover=i
            j_crossover=j
            i+=1
            j+=1
        else:
            j+=1
    grootste_eind=max(sum(chrom1[i_crossover+1:]),sum(chrom2[j_crossover+1:]))  # som van staart indien nodig, 0 bij gelijke eindes
    som+=grootste_eind
    return som
