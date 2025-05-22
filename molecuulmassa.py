def atoommassa(tekstbestand):
    d={}
    with open(tekstbestand,'r') as file:
        regels= file.readlines()[1:]
        for regel in regels:
            atoomnummer, symbool, engels, nederlands,massa = regel.strip('\n').split('\t')
            d[symbool]=float(massa)
    return d

def molecuulmassa(formule, dic):
    mol_massa=0
    elementen= formule.split('-')
    for element in elementen:
        ind=None
        for index, teken in enumerate(element):
            if teken.isdigit():
                ind=index
                break
        if ind is None:
            if element not in dic:
                return int(-1)
            else:
                mol_massa+=dic[element]
        else:
            mol_massa+=dic[element[:ind]]*int(element[ind:])
    return mol_massa





    return mol_massa
index = atoommassa('periodiek_systeem.txt')