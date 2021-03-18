import random


def password_generator(length, num, special, upper):
    # Function takes a desired length, and three bools num, special, and upper
    # Strings that contain password elements
    password = ""
    options = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    special_chars = "!@#$%^&*()_-+=*"
    upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # My methond for doing this is to first add in the mandatory chars
    # If I add in a mandatory char, I also add in that entire set of random
    # chars to the options string.
    # first add in a random mandatory lowercase letter.
    password += options[random.randrange(26)]
    if num:
        password += numbers[random.randrange(10)]
        options += numbers
    if special:
        password += special_chars[random.randrange(15)]
        options += special_chars
    if upper:
        password += upper_chars[random.randrange(26)]
        options += upper_chars

    # After that I want to fill in the rest of the password with random characters
    # from options, which now contains all of the characters that we are
    # allowed to use in the password
    num_chars_needed = length - len(password)
    chars_needed = random.choices(options, k=num_chars_needed)
    password += "".join(chars_needed)

    # And finally we want to shuffle our password.
    password = "".join(random.sample(password, len(password)))
    return password

# Annd lastly here are some testing strings.
# print(f'8 lowercase {password_generator(8, False, False, False)}')
# print(f'8 everything {password_generator(8, True, True, True)}')
# print(f'8 number lowercase {password_generator(8, True, False, False)}')
# print(f'8 special lowercase {password_generator(8, False, True, False)}')
# print(f'8 upper lowercase {password_generator(8, False, False, True)}')
# print(f'8 number upper lowercase {password_generator(8, True, False, True)}')
# print(f'8 special upper lowercase {password_generator(8, False, True, True)}')
