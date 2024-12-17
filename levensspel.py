def initieer_populatie(n): #n bepaalt de grootte van de symmetrische nxn-matrix
    nxn=[]
    for i in range(n):
        rij=['S']*n
        nxn.append(rij)
    return nxn
def infecteer_populatie(matrix,infectie_coordinaten):
    if len(infectie_coordinaten) > 1:
        for coordinaat in infectie_coordinaten:
            getal1 = coordinaat[0]
            getal2 = coordinaat[1]
            matrix[getal1][getal2] = 'I'
    elif len(infectie_coordinaten) == 1:
        getal1 = infectie_coordinaten[0]
        getal2 = infectie_coordinaten[1]
        matrix[getal1][getal2] = 'I'
    return matrix
def bereken_kans(p,l):
    kans=1-(1-p)**l
    if kans>0.5:
        return 1
    return 0

def simuleer_tijdstap(populatiematrix, p):
    n = len(populatiematrix)
    nieuw = initieer_populatie(n)

    for i in range(n):
        for j in range(n):
            if populatiematrix[i][j] == 'I' or populatiematrix[i][j]=='R':
                nieuw[i][j] = 'R'
            elif populatiematrix[i][j] == 'S':
                buren = [
                    ((i - 1+n)%n, j), ((i + 1+n)%n, j), (i, (j - 1+n)%n), (i, (j + 1+n)%n),
                    ((i - 1+n)%n, (j - 1+n)%n), ((i - 1+n)%n, (j + 1+n)%n), ((i + 1+n)%n, (j - 1+n)%n), ((i + 1+n)%n, (j + 1+n)%n)]
                I_teller=0
                for coordinaat in buren:
                    x,y=coordinaat
                    if n>x>=0 and n>y>=0 and populatiematrix[x][y]=='I':
                        I_teller+=1
                if bereken_kans(p,I_teller)==1:
                    nieuw[i][j]='I'
                else:
                    nieuw[i][j]='S'
    return nieuw
def tel_populatie(matrix):
    som_s = 0
    som_i = 0
    som_r = 0

    for rij in matrix:
        s = rij.count('S')
        som_s+=s
        i = rij.count('I')
        som_i+=i
        r = rij.count('R')
        som_r+=r

    return(som_s,som_i,som_r)





