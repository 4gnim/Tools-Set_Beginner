import hashlib
import requests
import re

def check_password_strength(password):
    """
    Evaluates the strength of a password.
    """
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "length": length_error,
        "digit": digit_error,
        "uppercase": uppercase_error,
        "lowercase": lowercase_error,
        "symbol": symbol_error,
    }

    if all(not error for error in errors.values()):
        return "Strong", errors
    elif errors["length"]:
        return "Too Short", errors
    else:
        return "Weak", errors

def check_password_breach(password):
    """
    Checks if a password has been leaked using the Have I Been Pwned API.
    """
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        breaches = response.text.splitlines()
        for line in breaches:
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return True, int(count)
        return False, 0
    except requests.RequestException as e:
        print(f"Error checking password breach: {e}")
        return None, None

def main():
    print("Password Strength Analyzer & Breach Checker\n")
    password = input("Enter the password to check: ")

    # Check password strength
    strength, errors = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    if strength != "Strong":
        print("Issues:")
        if errors["length"]:
            print("- Password is too short (minimum 8 characters).")
        if errors["digit"]:
            print("- Add at least one digit.")
        if errors["uppercase"]:
            print("- Add at least one uppercase letter.")
        if errors["lowercase"]:
            print("- Add at least one lowercase letter.")
        if errors["symbol"]:
            print("- Add at least one special character (e.g., !@#$%^&*).")

    # Check password breach
    breached, count = check_password_breach(password)
    if breached is None:
        print("\nCould not verify if password has been breached due to network error.")
    elif breached:
        print(f"\nWARNING: This password has been leaked {count} times in data breaches. Consider changing it immediately!")
    else:
        print("\nGood news! This password has not been found in any known breaches.")

if __name__ == "__main__":
    main()
