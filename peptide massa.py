aminozuren='ACDEFGHIKLMNPQRSTVWY'
def is_aminozuur_sequentie(seq):
    for letter in seq:
        if letter not in aminozuren:
            return False
    return True
def peptide_of_eiwit(seq):
    if is_aminozuur_sequentie(seq):
        if len(seq)>=100:
            return False
        return True
def aantal_aminozuren(seq):
    hoeveel_per_soort=()
    for letter in aminozuren:
        aantal=seq.count(letter)
        hoeveel_per_soort+=(aantal,)
    return hoeveel_per_soort
def massa_aminozuren(aantal_per_soort):
    massa_lijst= [71.03711, 103.00919, 115.02694, 129.04259, 147.06841, 57.02146, 137.05891, 113.08406,
        128.09496, 113.08406, 131.04049, 114.04293, 97.05276, 128.05858, 156.10111, 87.03203,
        101.04768, 99.06841, 186.07931, 163.06333]
    massa=18.0153
    for index,getal in enumerate(aantal_per_soort):
        massa+= getal*massa_lijst[index]
    return float("{:5f}".format(massa))
def info_sequentie(seq):
    if is_aminozuur_sequentie(seq):
        massa=massa_aminozuren(aantal_aminozuren(seq))
        lengte=len(seq)
        if peptide_of_eiwit(seq):
            return f"Dit is een peptide van {lengte} aminozuren en een massa van {massa} Dalton"
        return f"Dit is een eiwit van {lengte} aminozuren en een massa van {massa} Dalton"
    return "Dat is geen aminozuursequentie"
