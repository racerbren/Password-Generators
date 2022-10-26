# Author: Brenden Bilson
# Date: October 26, 2022

import random


# Shuffle password
def shuffle(string) -> str:
    temp = list(string)
    random.shuffle(temp)
    return ''.join(temp)


# Generate 10 character long secure password using numbers and special characters
def make_password() -> str:
    # Generate 3 uppercase letters
    uc1 = chr(random.randint(65, 90))
    uc2 = chr(random.randint(65, 90))
    uc3 = chr(random.randint(65, 90))

    # Generate 3 lowercase letters
    lc1 = chr(random.randint(97, 122))
    lc2 = chr(random.randint(97, 122))
    lc3 = chr(random.randint(97, 122))

    # Generate 2 numbers
    n1 = chr(random.randint(48, 57))
    n2 = chr(random.randint(48, 57))

    # Generate 2 special characters
    sp1 = chr(random.randint(33, 152))
    sp2 = chr(random.randint(33, 152))

    # Now form password using every character and shuffle
    pw = uc1 + uc2 + uc3 + lc1 + lc2 + lc3 + n1 + n2 + sp1 + sp2
    pw = shuffle(pw)
    return pw


if __name__ == '__main__':
    ans = input('Would you like to use a auto-generated password? ')
    if ans.lower() == 'y' or ans.lower() == 'yes':
        new_pw = make_password()
        print('Your new password is ' + new_pw)
    else:
        print('No password created.')
