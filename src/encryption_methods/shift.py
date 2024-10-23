# Author: Alex
def shift_enc(plain_text, key, log):
    # a:65 z:90
    # A:65 B:90
    log.info(f"Shifting text by {key} character…")
    plain_text_shifted = ""
    for letter in plain_text:
        letter_shifted = chr(ord(letter) + key).upper()
        plain_text_shifted += letter_shifted
        log.debug(f"shifting '{letter}' to '{letter_shifted}'")
    return plain_text_shifted


# Author: Sirius
def shift_dec(cipher_text, key, log):
    # a:65 z:90
    # A:65 B:90
    pass


# Author: Alex
# Part 3.8
def break_shift(cipher_text):
    pass
