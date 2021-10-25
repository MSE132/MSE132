def egyenletek_kvíz(name, otos = 80, negyes = 70, harmas = 60, kettes = 50):
    '''Ez egy kvíz, ahol egyenletekkel kapcsolatban öt kérdést fogsz kapni, amit a végén a játék kiértékel és az
    outputban kiadja, hogy milyen jegyet kaptál rá. Az inputba írd be a neved, majd a ponthatárokat is megadhatod, ha nem
    az alapértelmezetteket szeretnéd. Ponthatárt százalékba adj meg százalékjel nélkül. (Alap ponthatárok: ötös = 80%
    felett, négyes = 70% felett, hármas = 60% felett és kettes = 50% felett.) A kérdésekre csak "a", "b", "c", vagy "d"-t
    válaszolhatsz.
    Pl.: egyenletek_kvíz("MSE", 85, 75, 65, 55)'''

    print("\nHelló %s!" % (name))
    print("""\nEz egy kvíz játék. Lesz 5 kérdés, és hozzájuk négy választási lehetőséged (A, B, C, D).
    Annak a válasznak a betűjelét kell majd beírnod, amelyiket igaznak hiszed.\n""")
    igen_nem = input("Készen állsz?").lower()
    if igen_nem == "igen":
        print("\nKezdődjék a játék!\n")
    else:
        raise ValueError("A játék végetért. Gyere vissza késöbb.")

    pontok = 0

    print("""Első kérdés:
    Mennyi az x?
    6x+8=11x–7
    A, x=6
    B, x=3
    C, x=2
    D, x=4""")
    valasz1 = input("Írd be a válaszod:").upper()
    if valasz1 == "B":
        print("\nHelyes válasz!")
        pontok = pontok + 2
    else:
        print("\nRossz válasz. A helyes válasz a B.")

    print("""\nMásodik kérdés:
    Mennyi az y?
    8*(y +10)–30=5y
    A, y=-50/3
    B, y=50/3
    C, y=10/3
    D, y=-10/3""")
    valasz2 = input("Írd be a válaszod:").upper()
    if valasz2 == "A":
        print("\nHelyes válasz!")
        pontok = pontok + 3
    else:
        print("\nRossz válasz. A helyes válasz az A.")

    print("""\nHarmadik kérdés:
    Peti, Robi és Sára együtt 34 évesek. Peti és Sára ikrek. Robi 10 évvel idősebb náluk.
    Milyen egyenlettel NEM lehet felírni a feldatot?
    A, 2(x-10)+x=34
    B, 2x+x+10=34
    C, 2x+(x+10)=34
    D, 2x-10+2=34""")
    valasz3 = input("Írd be a válaszod:").upper()
    if valasz3 == "D":
        print("\nHelyes válasz!")
        pontok = pontok + 4
    else:
        print("\nRossz válasz. A helyes válasz a D.")

    print("""\nNegyedik kérdés:
    Gondoltam egy kétjegyű számot. Hozzáadtam 14-et, a kapott szám felét vettem, majd az eredmény jegyeit felcseréltem.
    Így végül 84-et kaptam. Mennyi a gondolt szám?
    A, 72
    B, 154
    C, 82
    D, 96""")
    valasz4 = input("Írd be a válaszod:").upper()
    if valasz4 == "C":
        print("\nHelyes válasz!")
        pontok = pontok + 3
    else:
        print("\nRossz válasz. A helyes válasz a C.")

    print("""\nÖtödik kérdés:
    ((-x-2)*3+2x)/2<-9+x
    Mennyi x?
    A, x<1.5
    B, x<4
    C, x>1.5
    D, x>4""")
    valasz5 = input("Írd be a válaszod:").upper()
    if valasz5 == "D":
        print("\nHelyes válasz!")
        pontok = pontok + 5
    else:
        print("\nRossz válasz. A helyes válasz a D.")

    print("\nA maximális pontszám: 17 pont. Neked %s pontod lett." % (pontok))
    szazalek = int((pontok / 17) * 100)
    print(str(szazalek) + "%-os lett az eredményed.")
    if szazalek >= otos:
        vegeredmeny = 5
        print("5-ös lett a kvíz. Gratulálok %s!" % (name))
    elif szazalek >= negyes:
        vegeredmeny = 4
        print("4-es lett a kvíz. Csak így tovább!")
    elif szazalek >= harmas:
        vegeredmeny = 3
        print("3-as lett a kvíz. Még egy kis gyakorlás, és meglesz az 5-ös.")
    elif szazalek >= kettes:
        vegeredmeny = 2
        print("2-es lett a kvíz. Sok gyakorlás, és sikerülni fog. Ne add fel!")
    else:
        vegeredmeny = 1
        print("1-es lett a kvíz. Ne keseredj el! Sok gyakorlással még behozható a hátrány.")
    return vegeredmeny
