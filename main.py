#!/usr/bin/python3.5
# -*-coding:utf-8 -*

#IMPORTATION DES MODULES
import socket
import pickle
import time
import sys
import os
import hashlib
import RPi.GPIO as GPIO
from packages.donnee import *
from packages.message import *
from getpass import getpass

#Fonctions
def init_GPIO():
	num = 2
	GPIO.setmode(GPIO.BCM)
	while num < 28:
		GPIO.setup(num, GPIO.OUT)
		GPIO.output(num, GPIO.LOW)
		num += 1

#INITIALISATIONS
os.system(effacer)
os.chdir("/home/pi/")
GPIO.setwarnings(False)

with open('donnees_connexion.conf', 'rb') as fichier:		#Recuperation des donnes de connexion du fichier
	mon_depickler = pickle.Unpickler(fichier)
	donnee_connexion = mon_depickler.load()

init_GPIO()

#PROGRAMME MAIN()

message_bienvenue()

#Connection
while connexion:
	print("Veuillez vous identifier au système pour avoir acces aux commandes.\n")
	mot_de_passe = getpass("Mot de passe: ")
	mot_de_passe_1 = mot_de_passe.encode()
	mot_de_passe_chiffrer = hashlib.sha1(mot_de_passe_1).hexdigest()
	#Demande d'identification

	if mot_de_passe_chiffrer == donnee_connexion[0]:
		connexion = False				#Savoir si le mot de passe rentré est bon
		mdp = mot_de_passe
		os.system(effacer)
		print("\nIdentification reussie !\n")
	else:
		os.system(effacer)
		print("\nEchec de l'identification !\n\n")
		reesayer_c = input("Voulez vous reesayer ou quitter ? o pour oui et q pour quitter: ")	#Si echec alors question
		os.system(effacer)
		if reesayer_c.lower() == "q":
			print("Vous quittez le programme...")
			time.sleep(1.5)
			sys.exit(0)


#Boucle principal
while principal:
	while menu:
		message_menu()
		menu_i = input("Choisissez un nombre correspondant a une commande: ")	#Demande de choix
		if menu_i not in menu_l:
			os.system(effacer)
			print("\nVous avez rentrez une mauvaise donnee !")
			time.sleep(1.5)
			os.system(effacer)

		if menu_i == "1":
			menu = False	#Choix reseau
			reseau = True
		elif menu_i == "2":
			menu = False	#Choix etat
			etat = True
		elif menu_i == "3":
			menu = False	#Choix config
			config = True
		elif menu_i == "4":
			menu = False	#Choix changer mdp
			changer_mdp = True
		elif menu_i == "5":
			menu = False	#Choix reinitialiser
			reset = True
		elif menu_i == "6":
			menu = False	#Choix quitter
			quitter = True
		os.system(effacer)


	#Reseau
	if reseau:
		connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connexion_principale.bind((hote, port))
		connexion_principale.listen(5)
		print("Le serveur écoute à présent sur le port {}".format(port))
		print("Serveur en attente de connection...")
		connexion_avec_client, infos_connexion = connexion_principale.accept()
		print("Vous etes connecter avec l'addresse: {}".format(infos_connexion[0]))
		msg_recu = b""
		while msg_recu != b"quit":
			msg_recu = connexion_avec_client.recv(1024)		#/!\ METTRE INSTRUCTION GPIO
			print(msg_recu.decode())
			#if reseau_l[0] == "pin":
			#	GPIO_pin = int(reseau_l[1])
			#	if reseau_l[2] == "output" or reseau_l[2] == "input":
			#		if reseau_l[2] == "output":
			#			GPIO.setup(GPIO_pin, GPIO.OUT)
			#		elif reseau_l[2] == "input":
			#			GPIO.setup(GPIO_pin, GPIO.IN)

			#	if reseau_l[2] == "low" or reseau_l[2] == "high":
			#		if reseau_l[2] == "low":
			#			GPIO.output(GPIO_pin, GPIO.LOW)
			#		elif reseau_l[2] == "high":
			#			GPIO.output(GPIO_pin, GPIO.HIGH)

			#elif reseau_l[0] == "reset":
			#	pass

			#elif reseau_l[0] == "resetpin":
			#	init_GPIO()
			#	os.system(effacer)
			#	print("Port GPIO réinitialiser !")
			#	time.sleep(1.5)

			#elif reseau_l[0] == "quit":
			#	os.system(effacer)
			#	config = False
			#	menu = True

		print("Fermeture de la connection")
		connecxion_avec_client.close()
		connexion_principale.close()
		time.sleep(1.5)
		reseau = False
		menu = True

	#Etat
	elif etat:
		print("\nEtat des pins de la raspberry pi 3:\n")
		message_etat()
		etat_i = input("\nVoulez-vous quitter la page d'etat ? reset pour réinitialiser l'état des ports ou q pour quitter: ")
		if etat_i.lower() == "q":
			etat = False
			menu = True
		elif etat_i.lower() == "reset":
			pass


	#Config
	elif config:
		print("\nConfiguration des pins de la raspberry pi 3:\n")
		message_etat()
		message_options()
		config_i = input("\nQue voulez vous faire ? ")
		config_l = config_i.split(" ")
		if config_l[0] == "pin":
			GPIO_pin = int(config_l[1])
			if config_l[2] == "output" or config_l[2] == "input":
				if config_l[2] == "output":
					GPIO.setup(GPIO_pin, GPIO.OUT)
				elif config_l[2] == "input":
					GPIO.setup(GPIO_pin, GPIO.IN)
				elif config_l[2] == "pwm":
					p = GPIO.PWM(14, 20000)

			elif config_l[2] == "low" or config_l[2] == "high":
				if config_l[2] == "low":
					GPIO.output(GPIO_pin, GPIO.LOW)
				elif config_l[2] == "high":
					GPIO.output(GPIO_pin, GPIO.HIGH)
					
			elif int(config_l[2]) > 0 and int(config_l[2]) <= 100:
				if config_l[2] == "low":
					GPIO.output(GPIO_pin, GPIO.LOW)
				elif config_l[2] == "high":
					GPIO.output(GPIO_pin, GPIO.HIGH)

		elif config_l[0] == "reset":
			pass

		elif config_l[0] == "resetpin":
			init_GPIO()
			os.system(effacer)
			print("Port GPIO réinitialiser !")
			time.sleep(1.5)

		elif config_l[0] == "quit":
			os.system(effacer)
			config = False
			menu = True

		del config_l
		GPIO_pin = 0
		os.system(effacer)


	#Changer ou ajouter mdp
	elif changer_mdp:
		print("Mot de passe actuel:")
		print("    - {}".format(mdp))
		modif_1 = input("\nVoulez-vous vraiment modifier le mot de passe ? o pour oui, q pour quitter: ")
		if modif_1.lower() == "o":
			modif_2 = getpass("\nRentrez le mot de passe: ")
			modif_3 = getpass("\nRecommencez: ")
			if modif_2 == modif_3:
				modif_2 = modif_2.encode()
				donnee_connexion[0] = hashlib.sha1(modif_2).hexdigest()
				with open('donnees_connexion.conf','wb') as modif_5:
					modif_4 = pickle.Pickler(modif_5)
					modif_4.dump(donnee_connexion)
				print("Modification effectuee avec succes !")
				time.sleep(1.5)
				modif_mdp = False
				changer_mdp = False
				menu = True
			else:
				os.system(effacer)
				print("\nLes 2 mots de passe rentrés ne sont pas identiques !")
				time.sleep(1.5)
		elif modif_1.lower() == "q":
			os.system(effacer)
			changer_mdp = False
			menu = True
		else:
			os.system(effacer)
			print("Aucune commande c'est attribuer a cette lettre !")
			time.sleep(1.5)


	elif reset:
		reset_1 = getpass("Entrez le mot de passe superutilisateur: ")
		if hashlib.sha1(reset_1.encode()).hexdigest() == donnee_connexion[1]:
			donnee_connexion[0] = hashlib.sha1(b"romaing2").hexdigest()
			with open('donnees_connexion.conf', 'wb') as reset_2:
				reset_3 = pickle.Pickler(reset_2)
				reset_3.dump(donnee_connexion)
			os.system(effacer)
			print("Mot de passe réinitialiser en valeur par défaut à {}".format(donnee_connexion[0]))
			time.sleep(2.5)
			reset = False
			menu = True


	#Quitter
	elif quitter:
		principal = False
		os.system(effacer)
		print("\nVous quittez le serveur de gestion...")
		time.sleep(1.5)
		os.system(effacer)
		p.stop()
		sys.exit(0)


	os.system(effacer)
input("Appuyez sur la touche ENTREE pour continuer...")
