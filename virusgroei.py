p=float(input("Geef een decimaal getal tussen 0 en 100: "))
if 0<=p<=100:
    leerlingen_ziek=1
    leerlingen_gezond=41-leerlingen_ziek
    print(f"maandag {leerlingen_gezond} {leerlingen_ziek}")

    for days in range(2,6):
        besmettingskans=1-(1-p/100)**leerlingen_ziek
        nieuw_besmet=int(round(leerlingen_gezond*besmettingskans))
        leerlingen_ziek+=nieuw_besmet
        leerlingen_gezond-=nieuw_besmet
        dagen=["dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]
        dag=dagen[days-2]
        print(f"{dag} {leerlingen_gezond} {leerlingen_ziek}")

else:
    print("die waarde ligt niet tussen 0 en 100")


