import random

def ko_papir_ollo():
        '''Ez egy kő papír olló játék. A gép ellen játszol. Ha nyersz, akkor kapsz egy pontot, ha vesztesz levonódik egy pont.
        Döntetlennél nincs pontváltozás. A játék addig megy, amíg nem megy -10 alá a pontszámod, vagy nem írod be, hogy
        "kilépek". Kis betűkkel írjál és ékezettel.'''

        lista = ["kő", "papír", "olló"]
        lista2 = lista + ["kilépek"]
        x = 0
        while x > -10:
                my_choice = input("kő, papír, olló, kilépek")
                while my_choice not in lista2:
                        my_choice = input("Rossz input. Válassz az alábbiak közül: kő, papír, olló, kilépek")
                robot_choice = random.choice(lista)
                if my_choice == robot_choice:
                        print("Döntetlen")
                elif my_choice == "kilépek":
                        break
                elif my_choice == "kő":
                        if robot_choice == "papír":
                                print("Vesztettél")
                                x -= 1
                        else:
                                print("Nyertél")
                                x += 1
                elif my_choice == "olló":
                        if robot_choice == "papír":
                                print("Nyertél")
                                x += 1
                        else:
                                print("Vesztettél")
                                x -= 1
                else:
                        if robot_choice == "olló":
                                print("Vesztettél")
                                x -= 1
                        else:
                                print("Nyertél")
                                x += 1
                print("A te választásod: %s A gép választása: %s Az eddigi pontszámod: %s" %(my_choice, robot_choice, x))
