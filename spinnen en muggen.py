temperatuur=int(input("Geef een temperatuur: "))
if temperatuur<18:
    print("Het is nu te koud voor muggen")
elif temperatuur>=40:
    print("Het is nu te warm voor muggen")
else:
    groeifactor=(temperatuur-18)/21
    muggen=100
    spin=1
    for getal in range(11):
        print(f"week {getal} {muggen} {spin}")
        nieuwe_muggen=int(groeifactor*muggen)
        kans=1-(0.9**spin)
        opgegeten_muggen=int(kans*muggen)
        muggen+=nieuwe_muggen
        muggen-=opgegeten_muggen
        if opgegeten_muggen>=20:
            spin+=opgegeten_muggen//20

