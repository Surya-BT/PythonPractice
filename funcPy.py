# this is program to replicate the password generation

from random import randint
from random import choices
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from random import shuffle

def passGen_simple(n):
    ''' this function generates a simple password using lower case letters only.
    this function generates password with user-specified length
    input = length of password'''

    letters = 'abcdefghijklmnopqrstuvwxyz'
    max = len(letters)
    lst = [letters[randint(0,max-1)] for _ in range(n)]
    return ''.join(lst)

def passGen_simple_stdfn(n):
    '''this function makes use of the already defined functions in python to generate the simple password.
    input = length of password'''

    lst = choices(ascii_lowercase,k=n)
    return ''.join(lst)

def passGen_complex(n):
    '''most websites require that the password fulfil a predefined set of rules.
    - it should be atleast 8 characters long.
    - it should contain a uppercase character
    - it should contain a number
    - it should contain atleast a special character.
    This function generates a password that fulfils these rules.
    input = length of password'''

    if n<8:
        # if the lenght is less than 8, change it to a default setting of 8
        n=8

    
    splChar = '.,;:-_!$%&()='
    pswd = choices(ascii_lowercase,k=n-3)
    pswd += choices(ascii_uppercase,k=1)
    pswd += choices(digits,k=1)
    pswd += choices(splChar,k=1)
    shuffle(pswd)
    return ''.join(pswd)

# execution starts
pslen = 7

print(passGen_simple(pslen))
print(passGen_simple_stdfn(pslen))
print(passGen_complex(pslen))

