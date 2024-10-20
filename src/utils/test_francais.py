from .francais import francais


def test_francais_empty_string():
    assert francais("") == ""


def test_francais_single_word():
    assert francais("bonjour") == "bonjour"


def test_francais_sentence():
    assert francais("bonjour tout le monde") == "bonjour tout le monde"


def test_francais_with_punctuation():
    assert francais("bonjour, tout le monde!") == "bonjour, tout le monde!"


def test_francais_with_numbers():
    assert francais("bonjour 123") == "bonjour 123"


def test_francais_with_special_characters():
    assert francais("bonjour @ tout # le % monde") == "bonjour @ tout # le % monde"
