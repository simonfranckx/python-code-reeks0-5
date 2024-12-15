

def is_organic(molecuul,Atomen=('C','O','H','N','S')):
    molecuul=molecuul.replace('-','')
    getallen = '0123456789'
    for atoom in molecuul:
        if atoom not in Atomen and atoom not in getallen:
            return False
    return True


def atoms_molecule(molecuul,Atomen=('C','O','H','N','S')):
    atoom_telling = [0] * len(Atomen)
    i = 0
    while i < len(molecuul):
        if molecuul[i] in Atomen:  # Nieuw atoom gevonden
            atoom = molecuul[i]
            i += 1
            aantal = ''
            while i < len(molecuul) and molecuul[i].isdigit():
                aantal += molecuul[i]
                i += 1
            aantal = int(aantal) if aantal else 1  # Geen getal betekent 1
            if atoom in Atomen:
                index = Atomen.index(atoom)
                atoom_telling[index] += aantal
        else:
            i += 1  # Sla ongeldig karakter over
    return tuple(atoom_telling)


def molecule_mass(lijst):
    getallen=[12.01,15.99,1.01,14.01,32.07]
    massa=0
    for index,getal in enumerate(lijst):
        massa_nu=getal*getallen[index]
        massa+=massa_nu
    return massa
def mass_organic_molecule(molecuul):
    if is_organic(molecuul):
        telling=atoms_molecule(molecuul)
        massa=molecule_mass(telling)
        return f"the mass is {massa}"
    return "that is not an organic molecule"
