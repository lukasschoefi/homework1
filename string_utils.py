def clean_whitespace(text: str) -> str:
    """Entfernt überflüssige Leerzeichen aus einem Text."""
    return " ".join(text.split())

def count_words(text: str) -> int:
    """Zählt die Wörter in einem gegebenen Text."""
    return len(text.split())

def is_palindrome(text: str) -> bool:
    """Prüft, ob ein Text ein Palindrom ist (ignoriert Groß-/Kleinschreibung und Leerzeichen)."""
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1] if cleaned else False