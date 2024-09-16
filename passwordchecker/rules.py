import re

def is_long_enough(password):
    """Verifică dacă parola are cel puțin 8 caractere."""
    return len(password) >= 8

def contains_uppercase(password):
    """Verifică dacă parola conține cel puțin o literă mare."""
    return any(char.isupper() for char in password)

def contains_lowercase(password):
    """Verifică dacă parola conține cel puțin o literă mică."""
    return any(char.islower() for char in password)

def contains_number(password):
    """Verifică dacă parola conține cel puțin un număr."""
    return any(char.isdigit() for char in password)

def contains_special_character(password):
    """Verifică dacă parola conține cel puțin un caracter special."""
    return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
