import pickle
import hashlib
import os

mdp = []
mdp.append(hashlib.sha1(b"romaing2").hexdigest())
mdp.append(hashlib.sha1(b"macedoine224371").hexdigest())
os.chdir("/home/pi/")

with open('donnees_connexion.conf', 'wb') as fichier:
	mon_pickler = pickle.Pickler(fichier)
	mon_pickler.dump(mdp)

print("Information ecrite dans le fichier")
input("Appuyer sur la touche ENTREE pour continuer...")
