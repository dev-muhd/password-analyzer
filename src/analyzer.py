def check_min_length(password):
    return len(password) >= 8
    


def analyze_password(password):
    score = 0
    failures = []
    if check_min_length(password):
        score += 1
    else:
        failures.append("Password too short (minimum 8 characters)")

    return score, failures