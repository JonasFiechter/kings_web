from string import digits, ascii_letters, punctuation
from time import sleep
import sys
import re

#  Generates an valid index protecting the indexation of the string to be inside its limit
# Fixed the repeated values with the if and the recursion call (changed because the recursion limit)
def generate_index(index, limit, var, dict_, original_str):
    new_index = index + var
    while new_index > (limit - 1):
        new_index -= (limit - 1)
    while original_str[new_index] in dict_.values():
        new_index -= 1
    return new_index

#  Dict used to translate each character.
def generate_dict(var):
    original_str = digits + ascii_letters + punctuation
    cripto_dict = {}
    for index, item in enumerate(original_str):
        cripto_dict[item] = original_str[generate_index(index, len(original_str), var, cripto_dict, original_str)]
    return cripto_dict

def invert_dict(dict_):
    inverted = {}
    for manual_key, value in dict_.items():
        inverted[value] = manual_key
    return inverted

#  The idea for the key is to keep the var to generate the dictionary and the password
# The length of the password and the lenght of the key must be stored somewhere in the key
def generate_key(encrypted=0, key=0):
    security_key = '' + str(len(str(encrypted))) + '_' + str(len(str(key))) + '_'
    security_key += str(key) + str(encrypted)
    encrypted_name = re.sub(r'['+punctuation+']', '', encrypted).replace('\\', '')
    file_ = open(f'secret_key_{encrypted_name}.txt', 'w+')
    file_.write(f'{security_key}')
    file_.close()
    return security_key, encrypted_name

#  Each var is separated to make easy comprehension, *this app is about to help with academic and
# study purposes. A refactored and lightweight version will be published soon.
def read_key(file_path):
    file_ = open(f'{file_path}', 'r')
    content = file_.read().split('_')
    len_encrypted = content[0]
    len_key = content[1]
    key = content[2][:(int(len_key))]
    encrypted = content[2][int(len_key):]
    translated = translate(encrypted=encrypted, manual_key=int(key))
    return translated

def transform(password, dict_={}, manual_key=0):
    if not dict_:
        dict_ = generate_dict(manual_key)
    encrypted = ''
    for item in password:
        encrypted += dict_[item]
    print('Generating key')
    secret_key, key_name = generate_key(encrypted=encrypted, key=manual_key)
    print(f'your key => {secret_key} your file name => {key_name}.. check your folder and keep it safe!')
    return encrypted

def translate(encrypted, dict_={}, manual_key=0):
    if dict_:
        inverted_dict = invert_dict(dict_)
    else:
        inverted_dict = invert_dict(generate_dict(manual_key))
    original = ''
    for item in encrypted:
        original += inverted_dict[item]
    return original

def user_choice():
    choice = input('Press 0 to encrypt or 1 to translate: ')
    if choice != '0' and choice != '1':
        print('Wrong option, try again')
        return user_choice()
    return choice

#  Need to receive arguments to generate and read the key using sysargv (will be added soon)
#  Need to add key option to generate and save the file
if __name__ == '__main__':
    if user_choice() == '0':
        manual_key = int(input('input your manual_key: '))
        password = input('input your password: ')
        print('Processing...')
        encrypted = transform(password=password, manual_key=manual_key)
        print('\nDone!')
        print(f'Encrypted passoword => {encrypted}')
    else:
        manual_key = int(input('input your manual_key: '))
        encrypted = input('input your encrypted pass: ')
        print('Processing...')
        translated = translate(encrypted=encrypted, manual_key=manual_key)
        print('\nDone!')
        print(f'Translated passoword => {translated}')