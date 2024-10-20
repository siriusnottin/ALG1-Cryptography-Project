from .shift import shift_enc


class MockLogger:
    def __init__(self):
        self.messages = []

    def info(self, message):
        self.messages.append(message)

    def debug(self, message):
        self.messages.append(message)


def test_shift_enc():
    mock_log = MockLogger()
    shift_enc("abc", 1, mock_log)
    assert mock_log.messages == [
        "Shifting text by 1 character…",
        "shifting 'a' to 'B'",
        "shifting 'b' to 'C'",
        "shifting 'c' to 'D'",
    ]


def test_shift_dec():
    # Implement this test when shift_dec is defined
    pass


def test_break_shift():
    # Implement this test when break_shift is defined
    pass
