import passlib
import hashlib
import string
import itertools

from passlib.hash import sha512_crypt

hash = input('Enter the sha512 hash you would like to crack: ')
input_salt = input('Enter salt: ')
digits = int(input('Enter digits in the password: '))

def cracker(hash, input_salt, digits):
    dictionary = string.digits + string.ascii_letters
    for password in itertools.product(dictionary, repeat = digits):
        i = ''.join(password)
        crack = sha512_crypt.using(salt=input_salt, rounds=5000).hash(i)
        if crack == hash:
            print(f'SUCCESS!')
            correct = i 
            break
        else: 
            print(f'{i} - No dice... {crack}')

    print(f'The password is : {correct}')

cracker(hash, input_salt, 3)