import re

def check_password_strength(password):
    # Define criteria
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Calculate total score
    score = 0
    if not length_error:
        score += 1
    if not uppercase_error:
        score += 1
    if not lowercase_error:
        score += 1
    if not digit_error:
        score += 1
    if not special_char_error:
        score += 1

    # Determine password strength level
    if score == 5:
        strength = "Very Strong "
    elif score == 4:
        strength = "Strong "
    elif score == 3:
        strength = "Moderate "
    elif score == 2:
        strength = "Weak "
    else:
        strength = "Very Weak "

    # Feedback messages
    feedback = []
    if length_error:
        feedback.append(" Password should be at least 8 characters long.")
    if uppercase_error:
        feedback.append(" Add at least one uppercase letter.")
    if lowercase_error:
        feedback.append(" Add at least one lowercase letter.")
    if digit_error:
        feedback.append(" Add at least one number.")
    if special_char_error:
        feedback.append(" Add at least one special character (!, @, #, $, etc.)")

    return strength, feedback


# Main Program Loop
if __name__ == "__main__":
    print(" Password Strength Checker \n")

    while True:
        user_password = input("Enter your password: ")
        strength, feedback = check_password_strength(user_password)

        print(f"\nPassword Strength: {strength}\n")

        if strength == "Very Strong ":
            print(" Excellent! Your password meets all security requirements.")
            break  # Exit loop when password is strong enough
        else:
            print(" Your password does not meet all criteria. Please try again.\n")
            print("Suggestions to improve:")
            for tip in feedback:
                print(tip)
            print("\nPlease enter a new password.\n")
