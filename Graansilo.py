b= float(input("Geef de breedte van het veld: "))
l=float(input("Geef de lengte van het veld: "))
c=float(input("Geef de opbrengst per hectare: "))
r=float(input("Geef de straal van een silo: "))
h=float(input("Geef de hoogte van een silo: "))
aantal_graan= b*l*c/10000
import math
volume= math.pi*r**2*h
aantal_silos= int((aantal_graan//volume)+1)
print(aantal_silos)
graan_over= aantal_graan%volume
hoogte=graan_over/(math.pi*r**2)
print(hoogte)
#end