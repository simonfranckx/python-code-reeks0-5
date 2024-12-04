slogan=input("Geef een mysterieuze slogan: ")
p=int(input("Geef een startpositie: "))
s=int(input("Geef een stapgrootte: "))
lengte=len(slogan)
positie=p
nieuwe_slogan=""
for letter in range(0,lengte):
    nieuwe_positie=positie%lengte
    nieuwe_slogan+=slogan[nieuwe_positie]
    positie+=s
print(nieuwe_slogan)