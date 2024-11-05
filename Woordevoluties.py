woord=str(input("Geef een woord met enkel hoofdletters: ")).lower()
hoofdletter= str(input("Geef een hoofdletter: ")).lower()
alfabet="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
startpositie= alfabet.find(woord[0])
eindpositie= alfabet.find(hoofdletter,startpositie)
afstand=eindpositie-startpositie+1
for letter in woord:
    positie= alfabet.find(letter)
    eind= positie+afstand-1
    eindletter=alfabet[eind].upper()
    tussen= alfabet[positie+1:eind]     #niet inclusief op einde, geen -1 meer nodig
    letterup=letter.upper()
    print(f"{letterup}{tussen}{eindletter}")
    #end