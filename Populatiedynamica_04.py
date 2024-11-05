

gegevens=str(input("populatienaam,startaantal,groeisnelheid,tijd: "))
opgesplitst=gegevens.split(",")
populatienaam=opgesplitst[0]
startaantal=int(opgesplitst[1])
groeisnelheid=float(opgesplitst[2])
tijd=int(opgesplitst[3])
populatienaam=populatienaam.lower().strip()
if "populatie" in populatienaam:
    populatienaam=populatienaam.replace("populatie","").strip()          #else is niet altijd nodig
import math
aantal=int(startaantal*math.exp(groeisnelheid*tijd))
print("Er wordt verwacht dat de populatie {} groeit van {} naar {} op {} jaar tijd.".format(populatienaam,startaantal,aantal,tijd))
#end

