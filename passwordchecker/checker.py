from .rules import is_long_enough, contains_uppercase, contains_lowercase, contains_number, contains_special_character


def check_password_strength(password):
    """Evaluează puterea parolei pe baza mai multor criterii și returnează un scor."""
    score = 0

    if is_long_enough(password):
        score += 1
    if contains_uppercase(password):
        score += 1
    if contains_lowercase(password):
        score += 1
    if contains_number(password):
        score += 1
    if contains_special_character(password):
        score += 1

    return score


def evaluate_strength(password):
    """Returnează o evaluare a puterii parolei pe baza scorului."""
    score = check_password_strength(password)

    if score <= 2:
        return "Parola este slabă"
    elif score == 3:
        return "Parola este medie"
    else:
        return "Parola este puternică"
