#!/usr/bin/env python3


def lire(nom_fichier):
    f = open(nom_fichier, "r")
    f_content = f.read()
    f.close()
    return f_content


def shift_dec(cipher_text, key, log):
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
    text_file_path = os.path.join(DATA_DIR, "Les_Miserables.txt")
    output_file = os.path.join(OUTPUT_DIR, "Les_Miserables_decalage.txt")

    file_content_encrypted = shift_enc_file(text_file_path, key)
    ecrire(output_file, file_content_encrypted)

    output_key_file = os.path.join(OUTPUT_DIR, "key_shift.txt")
    ecrire(output_key_file, str(key))


def compter_lettres_majuscules(texte):
    letters_freq = {letter: 0 for letter in texte}
    for letter in texte:
        letters_freq[letter] += 1
    return letters_freq
