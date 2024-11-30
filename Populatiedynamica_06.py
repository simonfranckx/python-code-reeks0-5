import math
def bereken_tijd_tot_percentage_draagkracht(startaantal,r,draagkracht,percentage):
    aantal_op_tijdstip= startaantal
    tijdstip=0
    while draagkracht/(1+((draagkracht/startaantal-1)*math.exp(-r*tijdstip)))< draagkracht*percentage:
        tijdstip+=1
        aantal_op_tijdstip=int(draagkracht/(1+((draagkracht/startaantal-1)*math.exp(-r*tijdstip))))
    return tijdstip, aantal_op_tijdstip
print(bereken_tijd_tot_percentage_draagkracht(100,0.083,9000,0.99))

def vul_lijst_aan_met_max_tijdstip(populatie):
    populatie_lijst=populatie.split(',')
    naam=populatie_lijst[0]
    populatie_lijst=populatie_lijst[1:]
    populatie_lijst[0]=int(populatie_lijst[0])
    populatie_lijst[1]=float(populatie_lijst[1])
    populatie_lijst[2]=int(populatie_lijst[2])
    tijdstip,aantal= bereken_tijd_tot_percentage_draagkracht(populatie_lijst[0],populatie_lijst[1],populatie_lijst[2],0.99)
    populatie_lijst.append(tijdstip)
    populatie_lijst.append(aantal)
    print("Data "+str(naam)+": "+str(populatie_lijst))
    return naam, populatie_lijst
