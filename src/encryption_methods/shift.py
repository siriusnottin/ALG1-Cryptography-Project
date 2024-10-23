# Author: Alex
def shift_enc(plain_text, key, log):
    # we shift each letter by key number
    log.info(f"Shifting text by {key} character…")
    for letter in plain_text:
        letter_shifted = chr(ord(letter) + key).upper()
        log.debug(f"shifting '{letter}' to '{letter_shifted}'")


# Author: Sirius
def shift_dec(cipher_text, key, log):
    pass


# Author: Alex
def break_shift(cipher_text):
    pass
