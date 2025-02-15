def toevoegen_populatie(populaties,diersoort,populatienaam):
    if diersoort in populaties:
        populaties[diersoort].add(populatienaam)
    else:
        populaties[diersoort] = {populatienaam}


def verwijderen_populatie(populaties,diersoort,populatienaam=None):
    assert diersoort in populaties, "De opgegeven diersoort komt niet voor in de dictionary."
    if populatienaam:
        assert populatienaam in populaties[diersoort], "De opgegeven diersoort komt niet voor in de dictionary."
        populaties[diersoort].remove(populatienaam)
        if populaties[diersoort]== set():
            del populaties[diersoort]
    else:
        del populaties[diersoort]
