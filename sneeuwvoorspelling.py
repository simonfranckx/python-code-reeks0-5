import math
temperatuur= float(input("Geef een temperatuur: "))
if -20<=temperatuur<=20:
    dagen=['zondag','maandag','dinsdag','woensdag','donderdag','vrijdag']
    sneeuwhoogte=50
    for dag in dagen:
        sneeuwhoogte+=5
        print(f"{dag} {round(sneeuwhoogte)}")
        if temperatuur>=1:
            gesmolten_sneeuw=sneeuwhoogte/(1+math.exp((-25*temperatuur/sneeuwhoogte)+5))
            sneeuwhoogte-=gesmolten_sneeuw
else:
    print("dat is geen temperatuur tussen -20 en 20 graden Celsius")