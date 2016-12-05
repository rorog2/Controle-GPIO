from packages.message import *
from packages.donnee import *
import os
os.system("title Test des message, tableaux...")


print("Menu:")
print("    1 - Message menu")
print("    2 - Message etat")
print("    3 - Message bienvenue")
menu_i = input("Choisissez un nombre correspondant a une commande: ")	#Demande de choix
os.system(effacer)

if menu_i == "1":
	message_menu()
	os.system("pause")
elif menu_i == "2":
	message_etat()
	os.system("pause")
elif menu_i == "3":
	message_bienvenue()
	os.system("pause")