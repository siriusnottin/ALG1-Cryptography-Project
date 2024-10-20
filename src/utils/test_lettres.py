from .lettres import chaine_en_lettres


def test_chaine_en_lettres_empty_string():
    assert chaine_en_lettres("") == []


def test_chaine_en_lettres_single_character():
    assert chaine_en_lettres("a") == ["a"]


def test_chaine_en_lettres_multiple_characters():
    assert chaine_en_lettres("abc") == ["a", "b", "c"]


def test_chaine_en_lettres_with_spaces():
    assert chaine_en_lettres("a b c") == ["a", " ", "b", " ", "c"]


def test_chaine_en_lettres_with_special_characters():
    assert chaine_en_lettres("a!b@c#") == ["a", "!", "b", "@", "c", "#"]
