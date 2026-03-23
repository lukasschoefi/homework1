from string_utils import clean_whitespace, count_words, is_palindrome

def test_clean_whitespace():
    assert clean_whitespace("  hallo   welt  ") == "hallo welt"

def test_count_words():
    assert count_words("Das ist ein einfacher Test.") == 5

def test_is_palindrome():
    assert is_palindrome("Lagerregal") == True
    assert is_palindrome("Ein Neger mit Gazelle zagt im Regen nie") == True
    assert is_palindrome("Hallo") == False