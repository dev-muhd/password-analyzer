from analyzer import analyze_password

password = input("Enter password: ")
analyze_password(password)
score, failures = analyze_password(password)
print(f"Password score: {score}, Failures: {failures}")
