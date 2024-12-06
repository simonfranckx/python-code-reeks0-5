veld1=input("Geef een veld: ")
veld2=input("Geef het tweede veld: ")
letters='abcdefgh'
kolom1=letters.find(veld1[0])
kolom2=letters.find(veld2[0])
verschil=abs(kolom2-kolom1)
verschil2=abs(int(veld2[1])-int(veld1[1]))
if verschil==1 and verschil2+verschil==3 or verschil==2 and verschil2+verschil==3:
    print(f"het paard kan springen van {veld1} naar {veld2}")
else:
    print(f"het paard kan niet springen van {veld1} naar {veld2}")



