from .monoalphabetic import break_subst, subst_dec, subst_dec_key, subst_enc


def test_lire_clef_subst():
    # Assuming the function reads a key from a file, mock the file reading
    pass


def test_ecrire_clef_subst():
    # Assuming the function writes a key to a file, mock the file writing
    pass


def test_subst_enc():
    plain_text = "hello"
    key = "zyxwvutsrqponmlkjihgfedcba"
    expected_cipher_text = "svool"
    assert subst_enc(plain_text, key) == expected_cipher_text


def test_subst_dec_key():
    key = "zyxwvutsrqponmlkjihgfedcba"
    expected_dec_key = "abcdefghijklmnopqrstuvwxyz"
    assert subst_dec_key(key) == expected_dec_key


def test_subst_dec():
    cipher_text = "svool"
    key = "zyxwvutsrqponmlkjihgfedcba"
    expected_plain_text = "hello"
    assert subst_dec(cipher_text, key) == expected_plain_text


def test_break_subst():
    cipher_text = "svool"
    expected_plain_text = "hello"
    assert break_subst(cipher_text) == expected_plain_text
