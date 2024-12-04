scheidingsteken= input("Geef een scheidingsteken: ")
t= int(input("Geef het aantal regels: "))
for regel in range(0,t):
    gecodeerde_regel= input("Geef een gecodeerde regel: ")
    vind_scheiding= gecodeerde_regel.find(scheidingsteken)
    lengte=len(gecodeerde_regel)
    deel_1=gecodeerde_regel[:vind_scheiding]
    deel_2=gecodeerde_regel[vind_scheiding+1:lengte+1]
    decodeer=deel_2+deel_1
    print(decodeer)
