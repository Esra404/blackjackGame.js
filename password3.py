import random
import string

def generate_password(length):
    # Use the combination of lowercase letters, uppercase letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(generate_password(16))