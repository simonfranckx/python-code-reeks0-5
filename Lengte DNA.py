baseparen= float(input("Geef een schatting van het aantal baseparen per cel: "))
lengte_basepaar= float(input("Geef een schatting van de lengte van een enkel basepaar (in nanometer): "))
cellen= float(input("Geef een schatting van het totale aantal cellen in een menselijk lichaam: "))
lengte_meter= baseparen*lengte_basepaar/(10**9)*cellen
lengte_ae=lengte_meter/149597870691
zon_terug= lengte_ae/2
print(lengte_meter)
print(lengte_ae)
print(zon_terug)
#end
