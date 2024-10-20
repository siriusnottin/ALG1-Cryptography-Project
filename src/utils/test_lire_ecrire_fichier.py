import os
import tempfile

from .lire_ecrire_fichier import lire


class MockLogger:
    def __init__(self):
        self.messages = []

    def info(self, message):
        self.messages.append(message)


def test_lire_existing_file():
    mock_log = MockLogger()
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Hello, World!")
        temp_file_name = temp_file.name

    try:
        content = lire(temp_file_name, mock_log)
        assert content == "Hello, World!"
        assert mock_log.messages == [f"Reading file {temp_file_name}"]
    finally:
        os.remove(temp_file_name)


def test_lire_non_existing_file():
    mock_log = MockLogger()
    non_existing_file = "non_existing_file.txt"
    try:
        lire(non_existing_file, mock_log)
    except FileNotFoundError:
        assert True
    else:
        assert False
