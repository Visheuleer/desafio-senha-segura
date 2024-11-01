def check_length(password: str) -> bool:
    return len(password) >= 8


def check_uppercase(password: str) -> bool:
    return any(char.isupper() for char in password)


def check_digit(password: str) -> bool:
    return any(char.isdigit() for char in password)


def check_lowercase(password: str) -> bool:
    return any(char.islower() for char in password)


def check_special_characters(password: str) -> bool:
    special_characters = "!@#$%^&*()-+"
    return any(char in special_characters for char in password)