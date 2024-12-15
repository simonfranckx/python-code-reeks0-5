def initieerpopulatie(n): #n bepaalt de grootte van de symmetrische nxn-matrix
    nxn=[]
    for i in range(n):
        rij=['S']*n
        nxn.append(rij)
    return nxn
def infecteer_matrix(matrix,infectie_coordinaten):
    if len(infectie_coordinaten)>2:
        for coordinaat in infectie_coordinaten:
            getal1=coordinaat[0]
            getal2=coordinaat[1]
            matrix[getal1][getal2]='I'
    elif len(infectie_coordinaten)==2:
        getal1=infectie_coordinaten[0]
        getal2=infectie_coordinaten[1]
        matrix[getal1][getal2] = 'I'
    return matrix
def bereken_kans(p,l):
    kans=1-(1-p)**l
    if kans>0.5:
        return 1
    return 0
def simuleer_tijdstap(populatiematrix,p):
