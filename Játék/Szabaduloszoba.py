def szabaduloszoba():
    '''Ez a játék egy szabadulószoba. Opciók közül kell választanod, hogy mit szeretnél épp csinálni. Eldöntendő
    kérdésekre "igen" vagy "nem" választ adjál, ahol meg több lehetőséged van, ott mindig az adott döntésed betűjelét
    add meg. PL.: "b". A játék addig tart, amíg ki nem jutsz a szobából.'''
    i = 0
    key1 = False
    key2 = False
    nyitva = False
    print("Egy szobában találod magad. Az a célod, hogy minél hamarabb kijuss. (Csak kis betűkkel írj!)")
    szam = input("Mit teszel? a:Körülnézek, b:megnézem nyitva van-e az ajtó")
    if szam == "a":
        i = 2
    else:
        i = 1
        print("\nAz ajtó nincs nyitva, kéne hozzá egy kulcs.")
    while nyitva != True:
        if i == 1:
            if key1 == True:
                if input("Felhasználod a kulcsodat az ajtó kinyitására?") == "igen":
                    nyitva = True
                else:
                    print("Az ajtó továbbra sincs nyitva. Nézz körbe mégegyszer!")
                    i = 2
            elif key2 == True:
                print("\nA kulcs sajnos nem jó az ajtóba. Nézelődj tovább!")
                i = 2
            else:
                print("\nNincs kulcsod az ajtóhoz. Nézelődj tovább!")
                i = 2
        if i == 2:
            print("\nA szobában van egy íróasztal egy székkel, egy ablak, és egy utazóláda. Melyiket nézed meg?")
            szam = input("a:Az íróasztalt és a széket, b:Az ablakot, hátha nyitva van, c:Az utazóládát, d:Az ajtót")
            if szam == "a":
                i = 3
            elif szam == "b":
                i = 4
            elif szam == "c":
                i = 5
            else:
                i = 1
        if i == 3:
            if key2 == True:
                print("\nSemmi érdekeset nem találsz. Hova mész tovább?")
                szam = input("a:Megnézem az ablakot, b:Megnézem az utazóládát")
                if szam == "a":
                    i = 4
                else:
                    i = 5
            else:
                print("\nAz íróasztal fiókjában találsz egy kis kulcsot. Mit teszel?")
                key2 = True
                szam = input(
                    "a:Megnézem, hátha jó az ajtóba a kulcs, b:Megnézem nyitva-e az ablak, c:Megnézem az utazóládát")
                if szam == "a":
                    i = 1
                elif szam == "b":
                    i = 4
                else:
                    i = 5
        if i == 4:
            print("\nAz ablak nincs nyitva, így nem jutsz ki rajta. Nézelődj még egy kicsit!")
            i = 2
        if i == 5:
            if key1 == False:
                print("\nAz utazóláda zárva van.")
                if key2 == True:
                    if input("Megnézed, hogy a kulcsod jó-e bele?") == "igen":
                        key1 = True
                        print("\nKinyitod a ládát, és találsz benne egy nagyobb kulcsot. Mit teszel?")
                        szam = input("a:Megnézed, hogy jó-e az ajtóba a kulcs, b:Körülnézel mégegyszer")
                        if szam == "a":
                            i = 1
                        else:
                            i = 2
                    else:
                        print("A ládát továbbra sem tudod kinyitni. Nézelődj tovább!")
                        i = 2
                else:
                    print("Nézz körbe mégegyszer hátha megtalálod a kulcsát!")
                    i = 2
            else:
                print("\nA láda üres. Hova mész?")
                szam = input("a:Megnézed, hogy jó-e az ajtóba a kulcsod, b:Körülnézel mégegyszer")
                if szam == "a":
                    i = 1
                else:
                    i = 2
    print("\nGratulálok! Sikeresen kijutottál.")
