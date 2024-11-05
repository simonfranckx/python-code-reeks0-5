#invoer
a=int(input("Geef de waarde van parameter a: "))
b=int(input("Geef de waarde van parameter b: "))
n=int(input("Geef de tijd (in seconden) waarin je de proefbuis bestraalt: "))
t=int(input("Geef het aantal cellen in de proefbuis bij aanvang van experiment 2: "))
#experiment 1
s=int(0 )    #seconden
c=1     #cellen
for s  in range(0,n):
    cellen= a*c+b
    c=cellen
    s+=1
print("experiment #1:",c,"cellen na",n,"seconden")
#experiment 2
tijd=0 #seconden exp2
begincellen=t
while t<c: #hier is t nodig omdat er anders fouten komen bij 0 seconden: dan wordt eerst nog de celhoeveelheid berekent: je kan dus celhoeveelheid niet boven de lus zetten
    celhoeveelheid=a*t+b #dit mag niet boven de while lus staan want dan komen er fouten bij 0 seconden
    t=celhoeveelheid
    tijd+=1
print("experiment #2:",t,"cellen na",tijd,"seconden") #hier niet celhoeveelheid zetten maar t want anders komt er een fout bij het uitvoeren met tijd=0
