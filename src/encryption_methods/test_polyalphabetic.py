from .polyalphabetic import (
    ecrire_clef_poly,
    lire_clef_poly,
    poly_dec,
    poly_dec_key,
    poly_enc,
)


def test_lire_clef_poly():
    # Assuming the function reads a key from a file
    with open("test_key.txt", "w") as f:
        f.write("samplekey")
    assert lire_clef_poly("test_key.txt") == "samplekey"


def test_ecrire_clef_poly():
    # Assuming the function writes a key to a file
    ecrire_clef_poly("test_key.txt", "samplekey")
    with open("test_key.txt", "r") as f:
        assert f.read() == "samplekey"


def test_poly_enc():
    # Assuming the function encrypts plain text using a key
    assert poly_enc("hello", "key") == "riijv"  # Example output


def test_poly_dec_key():
    # Assuming the function decrypts a key
    assert poly_dec_key("riijv") == "key"  # Example output


def test_poly_dec():
    # Assuming the function decrypts cipher text using a key
    assert poly_dec("riijv", "key") == "hello"  # Example output
