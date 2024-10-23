# Author: @Alex
def lire(nom_fichier, log):
    log.info(f"Reading file {nom_fichier}")
    f = open(nom_fichier, "r")
    f_content = f.read()
    f.close()
    return f_content


# Author: @Alex
def ecrire(nom_fichier, texte, log):
    log.info(f"Writting file {nom_fichier}")
    f = open(nom_fichier, "w")
    f.write(texte)
