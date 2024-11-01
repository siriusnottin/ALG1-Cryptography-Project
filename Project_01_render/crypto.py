#!/usr/bin/env python3

import string

from unidecode import unidecode


def lire(nom_fichier):
    file = open(nom_fichier, "r")
    file_content = file.read()
    file.close()
    return file_content


def ecrire(nom_fichier, texte):
    file = open(nom_fichier, "w")
    file.write(str(texte))
    file.close()
    return None


def minuscules(texte):
    return texte.lower()


def shift_enc(plain_text, key):
    l = []
    plain_text_maj = plain_text.upper()
    plain_text_maj_accent = unidecode(plain_text_maj)

    for lettre in plain_text_maj_accent:
        if "A" <= lettre <= "Z":
            chiffrement = ord(lettre)
            chiffrement += key
            while chiffrement > 90:  # make sure its alphabetical
                chiffrement -= 26
            chiffrement = chr(chiffrement)
            l.append(chiffrement)
        else:
            l.append(str(lettre))
        k = "".join(l)
    return k


def shift_dec(cipher_text, key):
    decrypted_text = ""
    for letter in cipher_text:
        if letter.isalpha():
            letter_unshifted = chr(ord(letter) - key).lower()
            decrypted_text += letter_unshifted
        else:
            decrypted_text += letter
    return decrypted_text


# 2.3 Chiffrer texte
def shift_enc_file_mono_int(key):  # need to be called to encrypt file content
    text_encrypted = shift_enc_file(
        "Les_Miserables2.txt", key
    )  # Les_Miserables is too heavy to be processed. Created second file limited to the first 100 lines of og file
    ecrire("Les_Miserables_decalage.txt.", text_encrypted)
    ecrire("key_shift.txt", key)


def compter_lettres_minuscules(texte):
    d = {}
    for freq_lettres in texte:
        if 97 <= ord(freq_lettres) <= 122 and freq_lettres not in d:
            d[freq_lettres] = 1
        if 97 <= ord(freq_lettres) <= 122:
            d[freq_lettres] += 1
    return d


def compter_lettres_majuscules(texte):
    upper_letters = ""
    for letter in texte:
        if ord("A") <= ord(letter) <= ord("Z"):
            upper_letters += letter

    upper_letters_freq = {letter: 0 for letter in upper_letters}
    for letter in texte:
        upper_letters_freq[letter] += 1

    return upper_letters_freq


def max_lettres(freq_lettres):
    nums = list(freq_lettres.values())
    current_max_num = nums[0]
    for num in nums:
        if current_max_num < num:
            current_max_num = num
    for i in freq_lettres:
        if freq_lettres[i] == current_max_num:
            return i


def chaine_en_mots(texte):
    return texte.split()


def compter_mots(mots):
    words = mots
    words_freq = {word: 0 for word in words}
    for word in words:
        words_freq[word] += 1
    return words_freq


# Used as util in `break_subst` later
def compter_lettres(lettres):
    letters = lettres
    letters_freq = {letter: 0 for letter in letters}
    for letter in letters:
        letters_freq[letter] += 1
    return letters_freq


def max_mot_1(freq_mots):
    freq_mots = ""
    d = compter_mots(freq_mots)
    max_valeur = 0

    for mot, valeur in d.items():
        if valeur > max_valeur:
            freq_mots = mot
            max_valeur = valeur
    return freq_mots


def francais(texte):
    d = {}
    for lettre in texte:
        if lettre not in d:
            d[lettre] = 1
        else:
            d[lettre] += 1

    max_lettre = ""
    max_valeur = 0
    max_lettre2 = ""
    max_valeur2 = 0

    for lettre, valeur in d.items():
        if lettre.isalpha() and valeur > max_valeur:
            max_lettre = lettre
            max_valeur = valeur
        elif lettre.isalpha() and max_valeur2 < valeur < max_valeur:
            max_lettre2 = lettre
            max_valeur2 = valeur

    if max_lettre == "e" or max_lettre2 in ("a", "i"):
        print(texte)
        reponse = input("Est-ce du français ? Répondez par oui ou non : ")
        if reponse.lower() == "oui":
            return True
    else:
        return False


def break_shift(cipher_text):
    l = []
    for i in range(26):
        cipher_text_decrypt = shift_enc(unidecode(cipher_text), i)
        cipher_text_decrypt = cipher_text_decrypt.lower()
        if francais(cipher_text_decrypt):
            l.append(i)
    return l


# 3.9 Casser chiffrement
def decrypt_shift_text():
    shifted_text = break_shift("shift_cipher_text.txt")
    ecrire("shift_plain_text.txt", shifted_text)


def lire_clef_subst(nom_fichier):
    lettre_min = string.ascii_lowercase
    l = list(lettre_min)
    contenu = lire("key_subst_2.txt")
    d = {}
    for i in range(len(contenu)):
        d[l[i]] = contenu[i]
    return d


def ecrire_clef_subst(nom_fichier, clef):
    ecrire(nom_fichier, clef)


def subst_enc(plain_text, key):
    encrypted_text = ""
    for letter in plain_text:
        if letter.isupper():
            encrypted_text += key.get(letter.lower(), letter).upper()
        elif letter.islower():
            encrypted_text += key.get(letter, letter)
        else:
            encrypted_text += letter
    return encrypted_text


def subst_dec_key(key):
    key = lire_clef_subst("key_subst_2.txt")
    total = lire_clef_subst(key)
    decrypt_key = {value: key for key, value in total.items()}
    d = {}
    for i in decrypt_key:
        d[i] = decrypt_key[i]
    return d


def subst_dec(cipher_text, key):
    decrypted_text = ""
    for letter in cipher_text:
        if letter.isupper():
            decrypted_text += key[letter.lower()].upper()
        elif letter.islower():
            decrypted_text += key[letter]
        else:
            decrypted_text += letter
    return decrypted_text


def shift_enc_file(file_path, key):
    file_content = lire(file_path)
    return subst_enc(file_content, key)


# 4.6 Chiffrer le texte
def shift_enc_file_mono_dict(key):  # need to be called to encrypt file content
    text_encrypted = shift_enc_file(
        "Les_Miserables2.txt", key
    )  # Les_Miserables is too heavy to be processed. Created second file limited to the first 100 lines of og file
    ecrire("Les_Miserables_substitution.txt", text_encrypted)
    ecrire("key_subst.txt", key)


# 4.7 Chiffrer le fichier chiffré
def shift_enc_text_file_miserables(key=3):
    file_encrypted = shift_enc_file("Les_Miserables_substitution.txt", key)
    ecrire("Les_Miserables_substitution_2.txt", file_encrypted)
    ecrire("key_subst_2.txt", str(key))


# 5.1
def break_subst(cipher_text):
    # Use only upper letters for encrypted text
    cipher_letters = [l for l in cipher_text if l.isupper()]
    freq = compter_lettres(cipher_letters)

    freq_sorted = sorted(freq.items(), key=lambda item: item[1], reverse=True)

    cipher_to_plain = {}

    def display_frequencies():
        print("Fréquences des lettres dans le texte chiffré :")
        for letter, count in freq_sorted:
            print(f"{letter}: {count}")

    def display_mapping():
        print("\nMappings actuels :")
        for l in sorted(cipher_to_plain.keys()):
            print(f"{l} -> {cipher_to_plain[l]}")

    def decrypt_text():
        decrypted = ""
        for l in cipher_text:
            if l.isupper():
                if l in cipher_to_plain:
                    decrypted += cipher_to_plain[l]
                else:
                    decrypted += "_"
            else:
                decrypted += l  # Conserver les autres caractères tels quels
        return decrypted

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

    return cipher_to_plain, decrypt_text()


# 5.2 Déchiffrer texte
def uncrypt_text_mono():
    file = lire("subst_cipher_text.txt")
    (plain_text, key) = break_subst(file)
    ecrire("subst_plain_text.txt", plain_text)


# 5.3 Casser et déchiffrer fichier
def break_file_cipher_mono():
    file = "Les_Miserables_substitution_2.txt"
    (plain_text, key) = break_subst(file)
    ecrire("double_key.txt", key)


def lire_clef_poly(nom_fichier):
    nom_fichier = open("double_key.txt", "r")
    contenu = nom_fichier.read().strip()  # permet d'ignorer les espaces
    nom_fichier.close()
    k1 = []
    k2 = []
    for i in range(len(contenu)):
        if i < len(contenu) / 2:
            k1.append(contenu[i])
        else:
            k2.append(contenu[i])

    lettre_min = string.ascii_lowercase
    d1 = {lettre_min[i]: k1[i] for i in range(len(k1))}
    d2 = {lettre_min[i]: k2[i] for i in range(len(k2))}

    return d1, d2


def ecrire_clef_poly(nom_fichier, clef):
    ecrire(nom_fichier, (clef))


def poly_enc(plain_text, key):
    lettre_min = string.ascii_lowercase
    key = lire_clef_poly("double_key.txt")
    chiffrement = ""

    for i, lettre in enumerate(plain_text):
        sous_clé = key[i % len(key)]  # Pour alterner les clés
        if lettre in lettre_min:
            chiffrement += sous_clé[lettre]
        else:
            chiffrement += lettre  # pour garder la casse et l'appliquer comme tel
    return chiffrement


def poly_dec_key(key):
    decrypt_key = []
    for sub_key in key:
        inverted_sub_key = {value: k for k, value in sub_key.items()}
        decrypt_key.append(inverted_sub_key)
    return decrypt_key


def poly_dec(cipher_text, key):
    decrypted_text = ""
    for i, lettre in enumerate(cipher_text):
        sous_clé = key[i % len(key)]
        if lettre in sous_clé:
            decrypted_text += sous_clé[lettre]
        else:
            decrypted_text += lettre
    return decrypted_text


def encrypt_text_file_poly(key):
    file_content = lire("Les_Miserables.txt")
    encrypted_text = poly_enc(file_content, key)
    ecrire("Les_Miserables_polyalphabet.txt", encrypted_text)
    ecrire("key_poly.txt", key)
