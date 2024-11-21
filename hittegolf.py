temperatuur=0
stopwoord='stop'
teller=1
volgorde=[]
boven=''

while temperatuur != stopwoord:
    temperatuur=input("Geef een temperatuur: ")
    if temperatuur==stopwoord:
        break

    omgevormd=float(temperatuur)
    if omgevormd >= 25:
        volgorde.append(teller)
        teller += 1
    else:
        volgorde += '0'
        teller=1
    if omgevormd>=30:
        boven+='1'
    else:
        boven+='0'
geen_hittegolf=1
plaats=0
for getal in volgorde:
    plaats += 1
    cijfer=int(getal)
    if cijfer>=5 :
        plaats_boven= boven[plaats-cijfer+1:plaats+1]
        tropisch=plaats_boven.count('1')
        if tropisch>=3:
            print('hittegolf')
            geen_hittegolf*=0
            break


if geen_hittegolf==1:
    print('geen hittegolf')






