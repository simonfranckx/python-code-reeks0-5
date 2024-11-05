weging1= input("Geef de stand van de weegschaal na de eerste weging: ")
weging2= input("Geef de stand van de weegschaal na de tweede weging: ")
if weging1 == "evenwicht":
    if weging2 == "evenwicht":
     print("muntstuk #9 is vervalst")
    elif weging2 == "links":
     print("muntstuk #8 is vervalst")
    else:
     print("muntstuk #7 is vervalst")
elif weging1== "links":
    if weging2 == "evenwicht":
     print("muntstuk #6 is vervalst")
    elif weging2 == "links":
     print("muntstuk #5 is vervalst")
    else:
     print("muntstuk #4 is vervalst")
else:
    if weging2 == "evenwicht":
     print("muntstuk #3 is vervalst")
    elif weging2 == "links":
     print("muntstuk #2 is vervalst")
    else:
     print("muntstuk #1 is vervalst")
#end
