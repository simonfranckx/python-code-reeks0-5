#input
groeisnelheid= float(input("Geef de groeisnelheid van de populatie: "))
startaantal= int(input("Geef het startaantal van de populatie: "))
tijd= int(input("Geef de tijd in jaren die je wil bestuderen: "))
draagkracht= int(input("Geef de draagkracht van de populatie: "))
#uitvoer
import math
for n in range(1,6):
    populatiegrootte = int(draagkracht / (1 + ((draagkracht / startaantal) - 1) * math.exp(-groeisnelheid * n)))
    print("Tijdstip",n,"- populatiegrootte:",populatiegrootte)
for n in range(1,6,4):
    populatiegrootte = int(draagkracht / (1 + ((draagkracht / startaantal) - 1) * math.exp(-groeisnelheid * n)))
    if populatiegrootte>=draagkracht*99/100:
        print("99% van de draagkracht werd bereikt")
        print("Aantal jaren",n,"- populatiegrootte:",populatiegrootte)
        break
for n in range(5,tijd+1,5):
    populatiegrootte = int(draagkracht / (1 + ((draagkracht / startaantal) - 1) * math.exp(-groeisnelheid * n)))
    if populatiegrootte >= draagkracht * 99 / 100 and n<6:
        break
    if populatiegrootte>=draagkracht*99/100:
        print("99% van de draagkracht werd bereikt")
        print("Aantal jaren",n,"- populatiegrootte:",populatiegrootte)
        break
#end


