def check_min_length(password):
    return len(password) >= 8

def check_has_digit(password):
    return any(char.isdigit() for char in password)

def check_has_uppercase(password):
    return any(char.isupper() for char in password)
    


def analyze_password(password):
    score = 0
    failures = []
    if check_min_length(password):
        score += 1
    else:
        failures.append("Password too short (minimum 8 characters)")

    if check_has_digit(password):
        score += 1
    else:
        failures.append("Password must contain at least one digit")

    if check_has_uppercase(password):
        score += 1
    else:
        failures.append("Password must contain at least an uppercase letter")

    return score, failures