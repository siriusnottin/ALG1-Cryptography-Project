from .words import chaine_en_mots, compter_mots, max_mot_1


def test_chaine_en_mots_single_word():
    assert chaine_en_mots("hello") == ["hello"]


def test_chaine_en_mots_multiple_words():
    assert chaine_en_mots("hello world") == ["hello", "world"]


def test_chaine_en_mots_empty_string():
    assert chaine_en_mots("") == [""]


def test_chaine_en_mots_with_spaces():
    assert chaine_en_mots("  hello  world  ") == ["", "", "hello", "", "world", "", ""]


def test_compter_mots_single_word():
    assert compter_mots(["hello"]) == {"hello": 1}


def test_compter_mots_multiple_words():
    assert compter_mots(["hello", "world", "hello"]) == {"hello": 2, "world": 1}


def test_compter_mots_empty_list():
    assert compter_mots([]) == {}


def test_compter_mots_with_repeated_words():
    assert compter_mots(["test", "test", "test"]) == {"test": 3}


def test_compter_mots_mixed_words():
    assert compter_mots(["apple", "banana", "apple", "orange", "banana", "apple"]) == {
        "apple": 3,
        "banana": 2,
        "orange": 1,
    }


def test_max_mot_1_single_word():
    assert max_mot_1({"hello": 1}) == "hello"


def test_max_mot_1_multiple_words():
    assert max_mot_1({"hello": 2, "world": 1}) == "hello"


def test_max_mot_1_tie():
    assert max_mot_1({"hello": 2, "world": 2}) in ["hello", "world"]


def test_max_mot_1_empty_dict():
    assert max_mot_1({}) is None


def test_max_mot_1_mixed_words():
    assert max_mot_1({"apple": 3, "banana": 2, "orange": 1}) == "apple"
