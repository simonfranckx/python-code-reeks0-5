def codeer_letter(letter):
    letter = letter.lower()
    if letter=='k':
        letter='c'
    alfabet = 'abcdefghijlmnopqrstuvwxyz'
    plaats = alfabet.find(letter)
    kolom = (plaats+1) % 5
    if kolom==0:
        kolom=5
    rij = plaats // 5 + 1
    return (rij, kolom)



def decodeer_letter(rij, kolom):
    alfabet = 'ABCDEFGHIJLMNOPQRSTUVWXYZ'
    plaats = rij * 5 - (5 - kolom)-1
    letter = alfabet[plaats]
    return letter


def codeer(woord):
    sequence = ""
    for letter in woord:
        punten1, punten2 = codeer_letter(letter)
        sequence += '.' * punten1 + ' '
        sequence += '.' * punten2 + ' '
    return sequence.strip()


def decodeer(sequence):
    strings = sequence.split(' ')
    aantal = len(strings)
    woord = ''
    for i in range(0, aantal-1,2):
        aantal1 = strings[i].count('.')
        aantal2 = strings[i + 1].count('.')
        letter = decodeer_letter(aantal1, aantal2)
        woord += letter
    return woord


