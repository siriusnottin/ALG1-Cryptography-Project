from .shift import shift_dec, shift_enc


class MockLogger:
    def __init__(self):
        self.messages = []

    def info(self, message):
        self.messages.append(message)

    def debug(self, message):
        self.messages.append(message)


def test_shift_enc():
    mock_log = MockLogger()
    result = shift_enc("abc", 1, mock_log)
    assert result == "BCD"
    assert mock_log.messages == [
        "Shifting text by 1 character…",
        "shifting 'a' to 'B'",
        "shifting 'b' to 'C'",
        "shifting 'c' to 'D'",
    ]


def test_shift_enc_with_negative_key():
    mock_log = MockLogger()
    result = shift_enc("abc", -1, mock_log)
    assert result == "ZAB"
    assert mock_log.messages == [
        "Shifting text by -1 character…",
        "shifting 'a' to 'Z'",
        "shifting 'b' to 'A'",
        "shifting 'c' to 'B'",
    ]


def test_shift_dec():
    mock_log = MockLogger()
    result = shift_dec("BCD", 1, mock_log)
    assert result == "ABC"
    assert mock_log.messages == [
        "Shifting text by -1 character…",
        "shifting 'B' to 'A'",
        "shifting 'C' to 'B'",
        "shifting 'D' to 'C'",
    ]


def test_shift_dec_with_negative_key():
    mock_log = MockLogger()
    result = shift_dec("ZAB", -1, mock_log)
    assert result == "ABC"
    assert mock_log.messages == [
        "Shifting text by 1 character…",
        "shifting 'Z' to 'A'",
        "shifting 'A' to 'B'",
        "shifting 'B' to 'C'",
    ]


def test_shift_dec():
    # Implement this test when shift_dec is defined
    pass


def test_break_shift():
    # Implement this test when break_shift is defined
    pass
