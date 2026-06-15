with open("mots_de_passe.txt", "r") as fichier:
    mots_de_passe = [ligne.strip() for ligne in fichier]

print("Liste des mots de passe :")

for mdp in mots_de_passe:
    print(mdp)
