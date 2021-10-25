import math

def masodfokumegoldo(a, b, c):
    '''Ez a függvény megadja az ax^2 + bx + c = 0 egyenlet megoldásait. Inputba a-t, b-t, és c-t kell beírni, és
    outputban megkapod egy listában a megoldást/megoldásokat. Ha nincs megoldása üres listát kapsz.
    Pl.: print(masodfokumegoldo(1, -2, 0))'''
    z = ((b) * (b) - 4 * (a) * (c))
    if z > 0:
        print("2 megoldás van.")
        y = (((b) * -1 + math.sqrt(z)) / (2 * (a)))
        x = (((b) * -1 - math.sqrt(z)) / (2 * (a)))
        megoldas = [x, y]
    elif z == 0:
        print("1 megoldás van.")
        x = (((b) * -1 - math.sqrt(z)) / (2 * (a)))
        megoldas = [x]
    else:
        print("Error! Nincs megoldás.")
        megoldas = []
    return megoldas
