worp1= input("Geef het resultaat van de worp bij de eerste gevangene: ")
worp2= input("Geef het resultaat van de worp bij de tweede gevangene: ")
wie= input("Geef de gevangene die het resultaat van zijn worp ook als antwoord geeft: ")
if wie=="eerste":
    if worp1=="kop" and worp2=="kop":
        print("kop")
        print("munt")
    elif worp1=="kop" and worp2=="munt":
        print("kop")
        print("kop")
    else:
        if worp2==("kop"):
            print("munt")
            print("munt")
        else:
            print("munt")
            print("kop")
else:
    if worp2=="kop" and worp1=="munt":
        print("kop")
        print("kop")
    elif worp2==("kop") and worp1==("kop"):  #hier was het belangrijk om ook worp2== toe te voegen, elif deed dit niet?
        print("munt")
        print("kop")
    else:
        if worp1==("kop"):
            print("munt")
            print("munt")
        else:
            print("kop")
            print("munt")
#end
