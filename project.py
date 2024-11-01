#!/usr/bin/env python3
# TODO: remove shebang. It may be missinterpreted as off-topic

import string


def lire(nom_fichier):
    f = open(nom_fichier, "r")
    f_content = f.read()
    f.close()
    return f_content


def ecrire(nom_fichier, texte):
    f = open(nom_fichier, "w")
    f.write(texte)
    f.close()


def shift_dec(cipher_text, key):
    decrypted_text = ""
    for letter in cipher_text:
        letter_unshifted = chr(ord(letter) - key).lower()
        decrypted_text += letter_unshifted
    return decrypted_text


def shift_enc_text_file_miserables(key=3):
    """
    Encrypts the contents of "Les_Miserables.txt" using a shift cipher and writes the encrypted content to a new file.

    Args:
        key (int, optional): The shift key for the cipher. Defaults to 3.

    The function performs the following steps:
    1. Reads the content of "Les_Miserables.txt" from the DATA_DIR.
    2. Encrypts the content using a shift cipher with the specified key.
    3. Writes the encrypted content to "Les_Miserables_decalage.txt" in the OUTPUT_DIR.
    4. Writes the shift key to "key_shift.txt" in the OUTPUT_DIR.
    """
    file = "Les_Miserables.txt"
    output_file = "Les_Miserables_decalage.txt"

    file_content_encrypted = shift_enc_file(file, key)
    ecrire(output_file, file_content_encrypted)

    output_key_file = "key_shift.txt"
    ecrire(output_key_file, str(key))


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


def compter_lettres(text):
    letters_freq = {letter: 0 for letter in text}
    for letter in text:
        letters_freq[letter] += 1
    return letters_freq


def max_mot_1(freq_mots):
    pass


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


def compter_mots(mots):
    words = mots
    words_freq = {word: 0 for word in words}
    for word in words:
        words_freq[word] += 1
    return words_freq


# 3.9
def decrypt_shift_text():
    file = "shift_cipher_text.txt"
    keys = break_shift(file)
    key = keys
    if len(keys) > 0:
        key = keys[0]
    uncrypted_text = shift_dec(file, key)
    ecrire("shift_plain_text.txt", uncrypted_text)


def ecrire_clef_subst(nom_fichier, clef):
    ecrire(nom_fichier, str(clef))


def subst_enc(plain_text, key):
    lettre_min = string.ascii_lowercase
    plain_text = list(lettre_min)
    key = lire_clef_subst("/home/ayu/Bureau/Projet/Fonctions/fichier_clÃ©.txt")
    chiffrement = ""
    for i in range(len(key)):
        chiffrement += key[plain_text[i]]
    return chiffrement


def subst_dec_key(key):
    # Cette fonction doit déduire une clé de déchiffrement via la clé de chiffrement.
    # ELle renvoie sous forme de dictionnaire. Sans modifier key par rapport à la 4.3
    total = lire_clef_subst(key)
    decrypt_key = {value: key for key, value in total.items()}
    d = {}
    for i in decrypt_key:
        d[i] = decrypt_key[i]
    return d


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
