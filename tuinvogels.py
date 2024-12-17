soorten_vogels = [
    "Vink", "Keep", "Appelvink", "Groenling", "Sijs", "Goudhaantje", "Putter",
    "Pimpelmees", "Koolmees", "Kuifmees", "Staartmees", "Merel", "Huismus",
    "Ringmus", "Roodborst", "Winterkoning", "Boomkruiper", "Boomklever",
    "Spreeuw", "Zanglijster", "Heggenmus", "Kauw", "Ekster", "Gaai", "Sperwer",
    "Houtduif", "Tortel", "Halsbandparkiet"
]

tellijst = [0] * len(soorten_vogels)
soorten_vogels_lower = [soort.lower() for soort in soorten_vogels]

while True:
    waarneming = input("Geef een waarneming: ")

    if waarneming.lower() == "stop":
        aantal_waarnemingen = sum(tellijst)
        print(f"Je hebt {aantal_waarnemingen} vogelwaarnemingen opgeslagen.")


        resultaten = []
        for i in range(len(tellijst)):
            if tellijst[i] > 0:
                resultaten.append((soorten_vogels[i], tellijst[i]))


        for i in range(len(resultaten)):
            for j in range(i + 1, len(resultaten)):
                if resultaten[j][1] > resultaten[i][1]:
                    resultaten[i], resultaten[j] = resultaten[j], resultaten[i]

        for soort, aantal in resultaten:
            print(f"{soort} {aantal}")
        break

    else:
        if waarneming.lower() in soorten_vogels_lower:
            plaats = soorten_vogels_lower.index(waarneming.lower())  # Index vinden
            tellijst[plaats] += 1  # Aantal waarnemingen bijwerken
        else:
            print("Dat is niet een van de te tellen tuinvogels.")
