groot_getal=int(input())
totaal_loon=groot_getal
loon_getal=int(0)
n=1
current_loon=0
vorig_loon=0
stopwoord='stop'

while current_loon != stopwoord:
    current_loon = input()
    if current_loon != stopwoord:
        totaal_loon += int(current_loon)
        print("werknemer #{} fluistert €{}".format(n,totaal_loon))

        n+=1


    else:
        gemiddeld_loon=(totaal_loon-groot_getal)/(n-1)
        print("gemiddeld loon: €{:.2f}".format(gemiddeld_loon))
        break



