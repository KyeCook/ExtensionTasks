"""
Workshop 3 Week 4 Extension Task
Tasks : 1) Word Generator
        2) Automatic Password Generator
"""

# --- 1) Word Generator ---

import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALL_OF_ALPHA = "abcdefghijklmnopqrstuvwxyz"

word_format = input("% = Consonant | # = Vowel | * = Either\nOther inputs will be displayed as is\nEnter word format: \
").lower()
word = ""

for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(ALL_OF_ALPHA)
    else:
        word += kind

print(word)


# --- 2) Automatic Password Generator ---
import random

# SPECIALS = "!@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}|"
# ALPHA_LOWER = "abcdefghijklmnopqrstuvwxyz"
# ALPHA_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# NUMBERS = 123456789
#
# lower_case = 0
# upper_case = 0
# special_characters = 0
# numbers = 0
#
# lowest_length = int(input("Enter the lowest length allowed:"))
# highest_length = int(input("Enter the highest length allowed:"))
# lower_cases_required = int(input("Enter amount of lower cases required:"))
# upper_cases_required = int(input("Enter amount of upper cases required:"))
# special_characters_required = int(input("Enter amount of specials required:"))
# numbers_required = int(input("Enter amount of numbers required:"))
#
# password_requirements = lowest_length, highest_length, lower_cases_required, upper_cases_required,numbers_required, \
#     special_characters_required
#
# for requirement in password_requirements:
#     if password_requirements(1) >
