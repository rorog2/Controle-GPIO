import RPi.GPIO as GPIO
GPIO_l = []
GPIO_n = []

def message_bienvenue():
	print(" +----------------------------------------------------+")
	print(" | Bienvenue dans le serveur de gestion du ports GPIO |")
	print(" +----------------------------------------------------+\n")


def message_etat():
	n = 2
	n1 = 0
	n2 = 1
	GPIO_l = []
	GPIO_n = []
	while n < 28:
		GPIO_n.append(n)
		GPIO_l.append(GPIO.gpio_function(n))
		GPIO_l.append(GPIO.input(n))
		n += 1

	print(" +----------------------------------------------------------------------------+")
	for elt in GPIO_n:
		if elt < 10:
			elt_s = "0"+str(elt)
		else:
			elt_s = elt

		if GPIO_l[n1] == 0:
			IO = "SORTIE"
		elif GPIO_l[n1] == 1:
			IO = "ENTREE"

		if GPIO_l[n2] == 0:
			HL = "LOW"
		elif GPIO_l[n2] == 1:
			HL = "HIGH"

		print("    - Port {}:    I/O: {}, Etat: {}".format(elt_s, IO, HL))
		n1 += 2
		n2 += 2

	print(" +----------------------------------------------------------------------------+")
	del GPIO_l
	del GPIO_n

def message_menu():
	print("+--------------------------------------+")
	print("| Menu principal du serveur de gestion |")
	print("+--------------------------------------+")
	print("    1 - Ouvrir l'accès aux reseaux")
	print("    2 - Afficher l'état des ports GPIO")
	print("    3 - Changer l'état des ports GPIO")
	print("    4 - Modifier le mot de passe administrateur")
	print("    5 - Réinitialiser le mot de passe administrateur par défaut")
	print("    6 - Quitter\n")

def message_options():
	print("""\nModifier l'I/O d'une sortie: pin <numéro de pin> <output ou input ou pwm> """)
	print("""Modifier l'état d'une I/O: pin <numéro de pin> <low ou hign> """)
	print("""Modifier l'état d'une PWM: pin <numéro de pin> <pourcentage> """)
	print("""Remettre toutes les I/O en valeurs par défault: resetpin """)
	print("""Réinitialiser l'affichage des états des ports: reset """)
	print("""Retourner au menu principal: quit """)
