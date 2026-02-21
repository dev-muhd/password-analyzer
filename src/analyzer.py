WEAK_THESHOLD = 0.4
MEDIUM_THRESHOLD = 0.7

def check_min_length(password):
    return len(password) >= 8

def check_has_digit(password):
    return any(char.isdigit() for char in password)

def check_has_uppercase(password):
    return any(char.isupper() for char in password)
    
def check_has_lowercase(password):
    return any(char.islower() for char in password)

def check_has_special_char(password):
    special_characters = "!@#$%^&*()-_=+[]|;:',.<>?/"
    return any(char in special_characters for char in password)

def check_no_spaces(password):
    return " " not in password


def analyze_password(password):
    rules = [
        (check_min_length, "Password too short (minimum 8 characters"),
        (check_has_digit, "Password must contain at least one digit"),
        (check_has_uppercase, "Password must contain at least one uppercase letter"),
        (check_has_lowercase, "Password must contain at least one lowercase letter"),
        (check_has_special_char, "Password must contain at least one special character"),
        (check_no_spaces, "No space is allowed in the password")
    ]
    score = 0
    failures = []
    total_rule_count = len(rules)

    for rule_function, failure_message in rules:
        if rule_function(password):
            score += 1
        else:
            failures.append(failure_message)

    strength_ratio = score / total_rule_count
    if strength_ratio < WEAK_THESHOLD:
        strength_label = "Weak"
    elif strength_ratio < MEDIUM_THRESHOLD:
        strength_label = "Medium"
    else:
        strength_label = "Strong"

    return {
        "score": score,
        "total_rules": total_rule_count,
        "failures": failures,
        "strength": strength_label
    }