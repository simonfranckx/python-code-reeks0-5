def vrucht_toevoegen(mandje, vrucht, hoeveelheid=0):

    """
    Voegt een bepaalde hoeveelheid van een vrucht toe aan een mandje.

    >>> nieuw_mandje = {}
    >>> vrucht_toevoegen(nieuw_mandje, 'aardbeien', 10)
    >>> 'aardbeien' in nieuw_mandje
    True
    >>> nieuw_mandje['aardbeien']
    10
    >>> vrucht_toevoegen(nieuw_mandje, 'aardbeien', 25)
    >>> nieuw_mandje['aardbeien']
    35
    """
    if vrucht not in mandje:
        mandje[vrucht]=0
    mandje[vrucht]= (mandje[vrucht]) + hoeveelheid



