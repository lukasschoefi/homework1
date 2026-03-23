from string_utils import clean_whitespace, count_words, is_palindrome

def test_clean_whitespace():
    assert clean_whitespace("  hallo   welt  ") == "hallo welt"

def test_count_words():
    assert count_words("Das ist ein einfacher Test.") == 5

def test_is_palindrome():
    assert is_palindrome("Lagerregal")
    assert is_palindrome("Reliefpfeiler")
    assert not is_palindrome("Hallo")