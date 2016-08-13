"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""


def main():
    MIN_LENGTH = 5
    MAX_LENGTH = 15
    MIN_LOWER = 1
    MIN_UPPER = 1
    MIN_DIGIT = 1
    MIN_SPECIAL = 1
    SPECIAL_CHARS_REQUIRED = True
    SPECIALS = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and contain: ".format(str(MIN_LENGTH), str(MAX_LENGTH)))
    print("\t{} or more lowercase characters".format(str(MIN_LOWER)))
    print("\t{} or more uppercase characters".format(str(MIN_UPPER)))
    print("\t{} or more numbers".format(str(MIN_DIGIT)))
    if SPECIAL_CHARS_REQUIRED:
        print("\tand {} or more special characters: ", SPECIALS.format(str(MIN_SPECIAL)))
    password = input("> ")
    while not is_valid_password(password, MIN_LENGTH, MAX_LENGTH, SPECIAL_CHARS_REQUIRED, SPECIALS,
                                MIN_LOWER, MIN_UPPER, MIN_DIGIT, MIN_SPECIAL):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password, MIN_LENGTH, MAX_LENGTH, SPECIAL_CHARS_REQUIRED, SPECIALS,
                      MIN_LOWER, MIN_UPPER, MIN_DIGIT, MIN_SPECIAL):
    valid = False
    if MIN_LENGTH <= len(password) <= MAX_LENGTH:
        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 0
        for char in password:
            # count each kind of character
            if char.islower():
                count_lower += 1
            elif char.isupper():
                count_upper += 1
            elif char.isdigit():
                count_digit += 1
            elif char in SPECIALS:
                count_special += 1
        if SPECIAL_CHARS_REQUIRED:
            if count_lower >= MIN_LOWER and count_upper >= MIN_UPPER and count_digit >= MIN_DIGIT and count_special >= MIN_SPECIAL:
                valid = True
        else:
            if count_lower >= MIN_LOWER and count_upper >= MIN_UPPER and count_digit >= MIN_DIGIT:
                valid = True
    return valid


if __name__ == "__main__":
    main()