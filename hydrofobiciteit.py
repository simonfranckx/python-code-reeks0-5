def hydrofobiciteit(eiwitsequentie, hydro_dict):
    lijst = []
    for letter in eiwitsequentie:
        lijst.append(hydro_dict[letter])
    return lijst


def filter(datapunten, gewichten):
    aantal_datapunten = len(datapunten)
    aantal_gewichten = len(gewichten)
    lijst = []

    for i in range(aantal_datapunten - aantal_gewichten + 1):
        som_producten = sum(datapunten[i + j] * gewichten[j] for j in range(aantal_gewichten))
        som_gewichten = sum(gewichten)
        lijst.append(som_producten / som_gewichten)

    return lijst


def filterGemiddelde(datapunten, breedte=5):
    if breedte % 2 == 0:
        breedte += 1  # Zorgt ervoor dat breedte oneven blijft
    gewichten = [1] * breedte
    return filter(datapunten, gewichten)


def filterDriehoek(datapunten, breedte=5):
    if breedte % 2 == 0:
        breedte += 1  # Zorgt ervoor dat breedte oneven blijft

    half = breedte // 2
    gewichten = list(range(1, half + 2)) + list(range(half, 0, -1))

    return filter(datapunten, gewichten)
