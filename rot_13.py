#!/usr/bin/env python3

"""
functions = cleartext, ciphertext, display_message
"""

key = 'abcdefghijklmnopqrstuvwxyz'


def main():
    cleartxt = cleartext()
    cipher = encrypt(cleartxt)
    plain = decrypt(cipher)
    printer(cipher, plain, cleartxt)


def cleartext():
    message = input('Enter the message: ')

    return message


def encrypt(cleartext):
    """
    take the message, split into individual char, rotate, put back

    :param cleartext:
    :return:
    """

    result = ''

    for letter in cleartext.lower():
        try:
            i = (key.index(letter) + 13) % 26
            result += key[i]
        except ValueError:
            result += ' '

    return result.lower()


def decrypt(cipher):
    result = ''

    for letter in cipher.lower():
        try:
            i = (key.index(letter) - 13) % 26
            result += key[i]
        except ValueError:
            result += ' '

    return result


def printer(cipher, plain, cleartext):
    print(f'Message: {cleartext}')
    print(f'Cipher: {cipher}')
    print(f'Plaintext: {plain}')


def display_message():
    pass


if __name__ == '__main__':
    main()
