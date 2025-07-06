import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short. Use at least 12 characters.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check for symbols
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (!, @, #, etc.)")

    # Evaluate
    if score >= 6:
        strength = "🔐 Very Strong"
    elif score >= 4:
        strength = "✅ Strong"
    elif score >= 3:
        strength = "⚠ Weak"
    else:
        strength = "❌ Very Weak"

    return strength, feedback

if __name__== "_main_":
    print("=== AI Password Strength Checker ===")
    pwd = input("Enter a password to check: ")
    strength, advice = check_password_strength(pwd)
    print(f"\nPassword Strength: {strength}")
    
    if advice:
        print("Suggestions to improve:")
        for tip in advice:
            print("- " + tip)
    else:
        print("Your password looks great!")