p=float(input("Geef een decimaal getal tussen 0 en 100: "))
if 0<=p<=100:
    leerlingen_ziek=1
    leerlingen_gezond=41-leerlingen_ziek
    print(f"dag 1,aantal gezonde leerlingen:{leerlingen_gezond},aantal zieke leerlingen:{leerlingen_ziek}")

    for days in range(2,6):
        besmettingskans=1-(1-p/100)**leerlingen_ziek
        nieuw_besmet=int(leerlingen_gezond*besmettingskans)
        leerlingen_ziek+=nieuw_besmet
        leerlingen_gezond-=nieuw_besmet
        print(f"dag {days}, aantal gezonde leerlingen: {leerlingen_gezond}, aantal zieke leerlingen: {leerlingen_ziek}")

else:
    print("die waarde ligt niet tussen 0 en 100")


