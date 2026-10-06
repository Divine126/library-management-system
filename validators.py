import re


def validate_isbn(text):
    clean = text.replace("-", "").replace(" ", "")
    pattern = r"^\d{10}$|^\d{13}$"
    return bool(re.fullmatch(pattern, clean))

def validate_email(text):
    pattern = r"^[^\s@]+@[^\s@]+\.[a-zA-Z]+$"
    return bool(re.fullmatch(pattern, text))

def validate_phone(text):
    pattern = r"^\+?\d{10,15}$"
    return bool(re.fullmatch(pattern, text))