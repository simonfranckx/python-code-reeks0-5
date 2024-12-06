import math
hoek1=float(input("Geef een hoek: "))
hoek2=float(input('Geef nog een hoek: '))
hoek3=float(input('Geef een laatste hoek: '))
rad=math.radians(hoek3)
x=(hoek2-hoek1+180)%360-180
sinus=math.sin(rad)
y=15*math.log((1+sinus)/(1-sinus),math.e)
print(f"x: {x}")
print(f"y: {y}")