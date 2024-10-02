import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters for better security.")
        return None

    # Defining possible characters
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensuring the password has at least one lowercase, one uppercase, one digit, and one special character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Filling the rest of the password with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffling the password list to make it random
    random.shuffle(password)

    # Joining the list into a string
    return ''.join(password)

# Main function to prompt user and display the generated password
def main():
    try:
        length = int(input("Enter the desired length of the password (minimum 4): "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
