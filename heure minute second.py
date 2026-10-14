X=str(input("Est ce que tu veux les heures et minutes sans second "))
if X=="oui" or X=="Oui":
    h=int(input("Donner moi l'heure "))
    m=int(input("Donner moi minute "))
    if h>=0 and h<24 and m>=0 and m<60:
        if h==23 and m==59:
            print("Dans une minute,il sera 00 heure(s) et 00")
        elif h<23 and m==59:
            print("Dans une minute,il sera ",h+1," heure(s) et 00")
        elif h>=0 and h<=23 and m>=0 and m<59:
            print("Dans une minute,il sera ",h," heure(s) et ",m+1)
elif X=="non" or X=="Non":
    h=int(input("Donner moi l'heure "))
    m=int(input("Donner moi minute ")) 
    s=int(input("Donner moi second "))
    if h>=0 and h<24 and m>=0 and m<60 and s>=0 and s<60:
        if h==23 and m==59 and s==59:
            print("Dans une second,il sera 00 heure(s) et 00 minute(s) et 00 second(s)")
        elif h<23 and m==59 and s==59:
            print("Dans une second,il sera ",h+1," heure(s) et 00 minute(s) et 00 second(s)")
        elif h<=23 and m<59 and s==59:
            print("Dans une second,il sera ",h," heure(s) et ",m+1," minute(s) et 00 second(s)")
        elif h<=23 and m<=59 and s<59:
            print("Dans une second,il sera ",h," heure(s) et ",m," minute(s) et ",s+1," second(s)")