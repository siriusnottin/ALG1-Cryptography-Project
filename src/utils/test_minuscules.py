from .minuscules import minuscules


def test_minuscules_all_uppercase():
    assert minuscules("HELLO") == "hello"


def test_minuscules_mixed_case():
    assert minuscules("HeLLo WoRLD") == "hello world"


def test_minuscules_all_lowercase():
    assert minuscules("hello") == "hello"


def test_minuscules_with_numbers():
    assert minuscules("Hello123") == "hello123"


def test_minuscules_with_special_characters():
    assert minuscules("Hello!@#") == "hello!@#"
