def issleutel(k1,k2):
    alfabet="abcdefghijklmnopqrstuvwxyz"
    k1=str(k1)
    k2=str(k2)
    fout=1
    if len(k1)!=13 or len(k2)!=13:
        fout*=0
    for letter in alfabet:
        if k1.lower().count(letter)+k2.lower().count(letter)==1:
            fout+=0
        else:
            fout*=0
    if fout==1:
        return True
    return False

#codeer_karakter
def codeer_karakter(c,k1,k2):
    vind_c_k1=k1.lower().find(c.lower())
    codeert_in_2= k2[vind_c_k1]
    vind_c_k2=k2.lower().find(c.lower())
    codeert_in_1=k1[vind_c_k2]
    if vind_c_k1>=0:
        if c==c.upper():
            return codeert_in_2.upper()
        else:
            return codeert_in_2.lower()

    elif vind_c_k2>=0:
        if c==c.upper():
            return codeert_in_1.upper()
        else:
            return codeert_in_1.lower()
    else:
        return c
#codeer
def codeer(message,k1,k2):
    gecodeert=""
    for letter in message:
        omgevormd=codeer_karakter(letter,k1,k2)
        gecodeert+=omgevormd
    return gecodeert

#decodeer (zelfde als codeer)
def decodeer(message,k1,k2):
    gecodeert=""
    for letter in message:
        omgevormd=codeer_karakter(letter,k1,k2)
        gecodeert+=omgevormd
    return gecodeert
