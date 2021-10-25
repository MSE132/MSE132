def gondoltszam(szam = 5):
	'''Ebben a játékban ki kell találnod, hogy melyik számra gondolt a gép. A gép random egy 1 és 100 közötti
	számra gondol. Hetet tippelhetsz, hogy mi lehetett a gondolt szám. Tippelés után a gép megadja, hogy eltaláltad-e
	és ha nem, akkor kisebb vagy nagyobb a gondolt szám. Inputba add meg, hogy mennyi kört szeretnél játszani. Alapból
	öt kör van.'''
	import random
	for i in range(szam):
		print("Új kör. Gondoltam egy számot 1 és 100 között. 7 próbálkozásod lesz.")
		number = random.randint(1, 100)
		for n in range(7):
			x = int(input("Írj be egy számot: "))
			if x == number:
				print("Ügyes vagy. Helyes válasz.")
				break
			elif x > number:
				print("Kisebb számot tippelj!")
			else:
				print("Nagyobb számot tippelj!")
