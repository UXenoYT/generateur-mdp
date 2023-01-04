#importer le module random
import random

#pré-générer la longueur du mot-de-passe
lenght_generator = random.randint(8,14)

#mettre en variable toutes les touches du clavier
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '@#()[]!*:/\_-=+$%&;.,?'

#additionner les 4 variables
all = lower + upper + numbers + symbols

#appliquer la longueur du mot de passe
lenght = lenght_generator

#générer le mot de passe
password = ''.join(random.sample(all, lenght))

#afficher le mot de passe dans la console
print('Le mot de passe est :', password)