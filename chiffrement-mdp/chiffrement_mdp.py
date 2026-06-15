import hashlib

with open("../fichier-mdp/mots_de_passe.txt", "r") as fichier:
    mots_de_passe = [ligne.strip() for ligne in fichier]

with open("mdp_hashes.txt", "w") as sortie:
    for mdp in mots_de_passe:
        hash_mdp = hashlib.sha256(mdp.encode()).hexdigest()
        sortie.write(hash_mdp + "\n")

print("Hachage terminé.")
