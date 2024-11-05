vragen=int(input("Geef het aantal vragen die in de ronde gesteld worden: "))
aantal=1
punten_uitdager=0
punten_crack=0
for aantal in range(1,vragen+1):
    juiste_antwoord= str(input(f"Geef het juiste antwoord op vraag {aantal}: "))
    antwoord_uitdager=str(input(f"Geef het antwoord van de uitdager op vraag {aantal}: "))
    oordeel_crack=str(input(f"Geef de beoordeling van de crack over het antwoord van de uitdager op vraag {aantal}: "))
    if antwoord_uitdager==juiste_antwoord:
        punten_uitdager+=1
        if oordeel_crack=='juist':
            punten_crack+=1
        else:
            punten_crack+=0
    else:
        punten_uitdager+=0
        if oordeel_crack=='fout':
            punten_crack+=1
        else:
            punten_crack+=0
if punten_crack < punten_uitdager or punten_crack < vragen / 2:
    print("uitdager wint met", punten_uitdager, "punten tegen", punten_crack)
elif punten_crack>punten_uitdager:
    print("crack wint met",punten_crack,"punten tegen",punten_uitdager)
else:
    print("ex aequo: beide deelnemers hebben", punten_crack, "punten")
#end








