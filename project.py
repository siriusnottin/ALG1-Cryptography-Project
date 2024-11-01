#!/usr/bin/env python3
# TODO: remove shebang. It may be missinterpreted as off-topic

import string

from unidecode import unidecode


def lire(nom_fichier):
    f = open(nom_fichier, "r")
    f_content = f.read()
    f.close()
    return f_content


def ecrire(nom_fichier, texte):
    f = open(nom_fichier, "w")
    f.write(texte)
    f.close()


def minuscules(texte):
    return texte.lower()


def shift_enc(plain_text, key):
    ligne = (
        plain_text.splitlines()
    )  # Ce bloc va découper le texte pour ne prendre que les lignes
    if len(ligne) > 100:
        plain_text = "\n".join(
            ligne[:100]
        )  # sous forme d'une liste et les mettre en chaine de caractère. le \n est pour le saut de ligne et le [:100] pour le nb de lignes
    l = []  # l va être ma variable pour stocker les lettres en ord)
    plain_text_maj = plain_text.upper()  # Cette fonction va permettre que la chaine de caractère de se transformer en majuscule et permettre à ma boucle while d'être pleinement fonctionnelle
    plain_text_maj_accent = unidecode(plain_text_maj)  #

    for lettre in plain_text_maj_accent:
        if "A" <= lettre <= "Z":
            chiffrement = ord(lettre)
            chiffrement += key  # On rajoute la key choisi augmenter la valeur ASCII
            while (
                chiffrement > 90
            ):  # boucle qui permet de revenir au début de l'alphabet
                chiffrement -= 26
            chiffrement = chr(chiffrement)
            l.append(chiffrement)
        else:
            l.append(str(lettre))
        k = "".join(l)  # k va être ma variable pour permettre d'enlever la liste
    return k


def shift_dec(cipher_text, key):
    decrypted_text = ""
    for letter in cipher_text:
        letter_unshifted = chr(ord(letter) - key).lower()
        decrypted_text += letter_unshifted
    return decrypted_text


# 2.3 Chiffrer texte
def shift_enc_file(file_path, key):
    file_content = lire(file_path)
    return shift_enc(file_content, key)


def compter_lettres_minuscules(texte):
    d = {}
    for freq_lettres in texte:
        if 97 <= ord(freq_lettres) <= 122 and freq_lettres not in d:
            d[freq_lettres] = 1
        if 97 <= ord(freq_lettres) <= 122:
            d[freq_lettres] += 1
    return d


def compter_lettres_majuscules(texte):
    # get all uppercase letters
    upper_letters = ""
    for letter in texte:
        if ord("A") >= letter <= ord("Z"):
            upper_letters += letter

    upper_letters_freq = {letter: 0 for letter in upper_letters}
    for letter in texte:
        upper_letters_freq[letter] += 1

    return upper_letters_freq


def max_lettres(freq_lettres):
    nums = list(freq_lettres.values())
    current_max_num = nums[0]
    # we sort the max_num list by descending order and get the first element that wil be our max
    for num in nums:
        if current_max_num < num:
            current_max_num = num
    for i in freq_lettres:
        if freq_lettres[i] == current_max_num:
            return i


def chaine_en_mots(texte):
    l = texte.split()
    return l


def compter_mots(mots):
    words = mots
    words_freq = {word: 0 for word in words}
    for word in words:
        words_freq[word] += 1
    return words_freq


def max_mot_1(freq_mots):
    texte = ""  # A voir
    d = {}
    texte = texte.split()
    for mot in texte:  # boucle qui va mettre chaque mot dans le dictionnaire
        if mot not in d:
            d[mot] = 1
        else:
            d[mot] += 1

    freq_mots = ""
    max_valeur = 0

    for mot, valeur in d.items():
        if valeur > max_valeur:
            freq_mots = mot
            max_valeur = valeur
    return freq_mots


def compter_lettres(text):
    letters_freq = {letter: 0 for letter in text}
    for letter in text:
        letters_freq[letter] += 1
    return letters_freq


def francais(texte):
    # la lettre la plus fréquente doit être le “e”
    # le mot à une lettre le plus fréquent doit être soit “a” soit “y”
    freq_letters = compter_lettres(texte)
    freq_mots = compter_mots(texte)
    is_french = False
    if max_lettres(freq_letters) == "e":
        is_french = True
    elif max_mot_1(freq_mots) in ("a", "y"):
        is_french = True
    return is_french


def break_shift(cipher_text):
    cipher_text_sans_accent = unidecode(cipher_text)  # à supprimer à la fin
    j = []
    for i in range(26):
        cipher_text_crypt = shift_enc(cipher_text_sans_accent, i)
        cipher_text_crypt = cipher_text_crypt.lower()
        if francais(cipher_text_crypt):
            j.append(i)
    return j


# 3.9 Casser chiffrement
def decrypt_shift_text():
    file = "shift_cipher_text.txt"
    keys = break_shift(file)
    key = keys
    if len(keys) > 0:
        key = keys[0]
    uncrypted_text = shift_dec(file, key)
    ecrire("shift_plain_text.txt", uncrypted_text)


def lire_clef_subst(nom_fichier):
    lettre_min = string.ascii_lowercase
    l = list(lettre_min)
    fichier = open("/home/ayu/Bureau/Projet/Fonctions/fichier_clé_mono.txt", "r")
    contenu = fichier.read()
    fichier.close()
    d = {}
    for i in range(
        len(contenu)
    ):  # Permet de voyager dans le contenu du fichier et i est itéré au nombre de fois.
        d[l[i % len(contenu)]] = contenu[
            i
        ]  # permet de prendre qu'un seul élément de la liste à ingrémenter dans le dictionnaire.
    return d


def ecrire_clef_subst(nom_fichier, clef):
    ecrire(nom_fichier, str(clef))


def subst_enc(plain_text: str, key: dict) -> str:
    """ "
    Encrypts the given plain text using a substitution cipher defined by the key dictionary.

    Args:
        plain_text (str): The text to be encrypted.
        key (dict): A dictionary mapping each letter of the plain text to its corresponding encrypted letter. Note: The encrypted letter will automatically by transformed in uppercase

    Returns:
        str: The encrypted text.
    """
    # Ensure all values in `key` are in lowercase
    key = {k: v.lower() for k, v in key.items()}

    encryted_text = ""
    for letter in plain_text:
        if letter.isupper():
            encryted_text += key[letter.lower()].upper()
        else:
            encryted_text += key[letter]
    return encryted_text


def subst_dec_key(key):
    # Cette fonction doit déduire une clé de déchiffrement via la clé de chiffrement.
    # ELle renvoie sous forme de dictionnaire. Sans modifier key par rapport à la 4.3
    total = lire_clef_subst(key)
    decrypt_key = {value: key for key, value in total.items()}
    d = {}
    for i in decrypt_key:
        d[i] = decrypt_key[i]
    return d


# TODO: Alex
def subst_dec(cipher_text, key):
    """
    Écrire une fonction subst_dec(cipher_text, key) qui prend une chaîne de caractères cipher_text et la clef de chiffrement sous forme de dictionnaire key et qui effectue le déchiffrement. La fonction renvoie le texte déchiffré sous forme de chaîne de caractères.
    """
    pass


# 4.6 Chiffrer le texte
# TODO: Sirius change fn name to `enc_file_mono`, maybe?
def shift_enc_text_miserables(key=3):
    text_encrypted = shift_enc_file("Les_Miserables.txt")
    ecrire("Les_Miserables_substitution.txt", text_encrypted)
    ecrire("key_subst.txt", str(key))


# 4.7 Chiffrer le fichier chiffré
def shift_enc_text_file_miserables(key=3):
    file_encrypted = shift_enc_file(" Les_Miserables_substitution.txt", key)
    ecrire("Les_Miserables_substitution_2.txt", file_encrypted)
    ecrire("key_subst_2.txt", str(key))


# 5.1
def break_subst(cipher_text):
    from collections import Counter

    # Ne considérer que les lettres majuscules pour le texte chiffré
    cipher_letters = [c for c in cipher_text if c.isupper()]
    freq = Counter(cipher_letters)

    # Trier les fréquences par ordre décroissant
    freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Initialiser le mapping des lettres chiffrées vers les lettres en clair
    cipher_to_plain = {}

    # Fonction pour afficher les fréquences
    def display_frequencies():
        print("Fréquences des lettres dans le texte chiffré :")
        for letter, count in freq_sorted:
            print(f"{letter}: {count}")

    # Fonction pour afficher le mapping actuel
    def display_mapping():
        print("\nMappings actuels :")
        for c in sorted(cipher_to_plain.keys()):
            print(f"{c} -> {cipher_to_plain[c]}")

    # Fonction pour déchiffrer le texte avec le mapping actuel
    def decrypt_text():
        decrypted = ""
        for c in cipher_text:
            if c.isupper():
                if c in cipher_to_plain:
                    decrypted += cipher_to_plain[c]
                else:
                    decrypted += "_"
            else:
                decrypted += c  # Conserver les autres caractères tels quels
        return decrypted

    # Boucle principale d'interaction avec l'utilisateur
    while True:
        display_frequencies()
        display_mapping()

        decrypted_text = decrypt_text()
        print("\nTexte déchiffré jusqu'à présent :")
        print(decrypted_text)

        # Demander à l'utilisateur d'entrer un mapping ou de quitter
        user_input = input(
            "\nEntrez 'lettre_chiffrée lettre_claire' pour ajouter/modifier un mapping, 'supprimer lettre_chiffrée' pour supprimer un mapping, ou 'quitter' pour terminer : "
        ).strip()

        if user_input.lower() == "quitter":
            break
        elif user_input.startswith("supprimer "):
            parts = user_input.split()
            if len(parts) == 2 and len(parts[1]) == 1 and parts[1].isupper():
                cipher_letter = parts[1].upper()
                if cipher_letter in cipher_to_plain:
                    del cipher_to_plain[cipher_letter]
                    print(f"Mapping pour {cipher_letter} supprimé.")
                else:
                    print(f"Aucun mapping n'existe pour {cipher_letter}.")
            else:
                print("Format d'entrée invalide pour supprimer un mapping.")
        else:
            parts = user_input.split()
            if len(parts) == 2 and len(parts[0]) == 1 and len(parts[1]) == 1:
                cipher_letter = parts[0].upper()
                plain_letter = parts[1].lower()
                if cipher_letter.isupper() and plain_letter.islower():
                    cipher_to_plain[cipher_letter] = plain_letter
                    print(f"Mapping mis à jour : {cipher_letter} -> {plain_letter}")
                else:
                    print(
                        "Veuillez entrer une lettre majuscule pour la lettre chiffrée et une lettre minuscule pour la lettre claire."
                    )
            else:
                print("Format d'entrée invalide.")

    # Retourner la clé trouvée et le texte déchiffré
    return cipher_to_plain, decrypt_text()
