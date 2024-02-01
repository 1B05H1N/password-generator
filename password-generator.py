"""
This Python program generates a secure, NIST-compliant password based on user preferences for length, 
inclusion of uppercase letters, numbers, and special characters. It ensures the generated password meets 
a minimum length of 12 characters, as recommended for machine-generated passwords, and includes a mix of 
character types to enhance complexity and security. The program also evaluates the strength of the generated 
password, categorizing it as 'Weak', 'Moderate', 'Strong', or 'Very Strong' based on its length, diversity, 
and uniqueness of characters. The final password is automatically copied to the clipboard for convenient use. 
"""

import secrets
import string
import pyperclip

def generate_nist_compliant_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    if length < 12:
        print("Increasing password length to meet NIST minimum standards.")
        length = 12

    char_set = string.ascii_lowercase
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_numbers:
        char_set += string.digits
    if use_special_chars:
        char_set += string.punctuation

    while True:
        password = ''.join(secrets.choice(char_set) for _ in range(length))
        if (not use_uppercase or any(char.isupper() for char in password)) and \
           (not use_numbers or any(char.isdigit() for char in password)) and \
           (not use_special_chars or any(char in string.punctuation for char in password)):
            break

    return password

def password_strength(password):
    strength = ['Weak', 'Moderate', 'Strong', 'Very Strong']
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    if len(set(password)) > len(password) / 2: 
        score += 1

    score = min(score, len(strength) - 1)
    return strength[score]

length = 12
use_uppercase = True
use_numbers = True
use_special_chars = True

password = generate_nist_compliant_password(length, use_uppercase, use_numbers, use_special_chars)
strength = password_strength(password)
print(f"Generated Password: {password} (Strength: {strength})")

pyperclip.copy(password)
print("Password copied to clipboard.")
