import math

def barmibol_barmire(mibol, mire, szam):
    '''Ez egy számrendszer átváltós program. inputba meg kell adnod, hogy melyik számrendszerbe van a szám amit megadsz,
    melyik számrendszerbe szeretnéd átváltani, és magát a számot. Outputban megkapod átváltva a számot. Egész számokat
    használj.
    PL.: print("A szám: %s" %(barmibol_barmire(2, 10, 101)))'''

    def tizesre(hanyas_szamrendszer, szam):
        betuk = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'w', 'x', 'y', 'z']
        vegso_szam = 0
        index = len(szam) - 1
        for i in szam:
            if i in betuk:
                vegso_szam += (hanyas_szamrendszer ** index) * (10 + betuk.index(i))
                index -= 1
            else:
                vegso_szam += (hanyas_szamrendszer ** index) * int(i)
                index -= 1
        return vegso_szam
    
    def tizesbol(szamrendszer, szam):
        betuk = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'w', 'x', 'y', 'z']
        eredeti_szam = szam
        x = 1
        vegso_szam = ""
        while x < szam:
            x = x * szamrendszer
        if x != 1:
            x = int(x / szamrendszer)
        while szam != 0:
            number = szam // x
            if number >= 10:
                vegso_szam = vegso_szam + betuk[number - 10]
            else:
                vegso_szam = vegso_szam + str(number)
            szam -= number * x
            x = int(x / szamrendszer)
        if eredeti_szam % szamrendszer == 0:
            vegso_szam = vegso_szam + str(szam)
        return vegso_szam

    szam = str(szam)
    tizesben_a_szam = tizesre(mibol, szam)
    vegso_szam = tizesbol(mire, tizesben_a_szam)

    return vegso_szam
