#input

startaantal= int(input("Geef het startaantal van de populatie: "))
groeisnelheid= float(input("Geef de groeisnelheid van de populatie: "))
draagkracht= int(input("Geef de draagkracht van de populatie: "))
percentages= [99,50]
#uitvoer
import math
def bereken_tijd_tot_percentage_draagkracht(groeisnelheid,startaantal,draagkracht,percentage):
    n=0
    while True:
        populatiegrootte = int(draagkracht / (1 + ((draagkracht / startaantal) - 1) * math.exp(-groeisnelheid * n)))
        if populatiegrootte>=(draagkracht*percentage/100):
            return n,populatiegrootte
        n+=1
for percentage in percentages:
    n,populatiegrootte=bereken_tijd_tot_percentage_draagkracht(groeisnelheid,startaantal,draagkracht,percentage)
    print(f"Na {n} jaar wordt {percentage}% van de draagkracht bereikt, dit zijn {populatiegrootte} dieren.")
#end







