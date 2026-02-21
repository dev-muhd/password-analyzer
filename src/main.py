from analyzer import analyze_password

password = input("Enter password: ")
result = analyze_password(password)

print(
    f"Password score: {result['score']}, "
    f"Total rules: {result['total_rules']}, "
    f"Failures: {result['failures']}, "
    f"Password strength: {result['strength']}"
)