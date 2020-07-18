# !/usr/bin/env python3

# check if a string is a palindrome
# palindrome_checker.py
# m. cook
# 7/18/2020


def get_string():
    """Prompt user to input a string"""
    print("Enter the word or phrase you want to test:")
    str = input()

    return str


def check_if_palindrome(str):
    """Check if the string is a palindrome"""
    # Filter string for non-letter characters
    if not str.isalpha():
        str = format_string(str)

    return str == str[::-1]


def format_string(str):
    """Make letters lower-case and remove any punctuation and whitespace"""
    letters = ''

    for character in str:
        character = character.lower()

        if character.isalpha():
            letters += character

    return letters


def main():
    str = get_string()

    if str == '':
        print("Error: no letters were entered")
    else:
        if check_if_palindrome(str):
            print("It's a palindrome!")
        else:
            print("It's not a palindrome.")


if __name__ == "__main__":
    main()
