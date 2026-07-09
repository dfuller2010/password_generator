import random
import string
import pyperclip


def get_user_options():
    length = int(input("Password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
    use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
    use_digits = input("Include numbers? (y/n): ").strip().lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"
    count = int(input("How many passwords? "))
    return length, use_upper, use_lower, use_digits, use_symbols, count

def get_character_set(use_upper, use_lower, use_digits, use_symbols):
    char_set = ""
    if use_upper:
        char_set += string.ascii_uppercase
    if use_lower:
        char_set += string.ascii_lowercase
    if use_digits:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation
    if char_set == "":
        print("You must select at least one character type. Defaulting to lowercase letters.")
        char_set = string.ascii_lowercase
    return char_set

def generate_password(length, char_set):
    password = ""
    for i in range(length):
        password += random.choice(char_set)
    return password

def display_passwords(passwords):
    print("\nYour generated passwords:")
    for i, password in enumerate(passwords):
        print(f"  {i + 1}. {password}")

def copy_to_clipboard(passwords):
    choice = input("\nEnter the number of the password to copy (or 0 to skip): ")
    choice = int(choice)
    if choice == 0:
        return
    pyperclip.copy(passwords[choice - 1])
    print(f"Password {choice} copied to clipboard!")

def main():
    length, use_upper, use_lower, use_digits, use_symbols, count = get_user_options()
    char_set = get_character_set(use_upper, use_lower, use_digits, use_symbols)
    
    passwords = []
    for i in range(count):
        passwords.append(generate_password(length, char_set))
    
    display_passwords(passwords)
    copy_to_clipboard(passwords)

main()