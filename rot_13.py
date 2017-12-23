#!/usr/bin/env python3

"""
functions = cleartext, ciphertext, display_message
"""

key = 'abcdefghijklmnopqrstuvwxyz'

def main():
    cleartxt = cleartext()
    cipher = encrypt(cleartxt)
    plain = decrypt(cipher)
    printer(cipher, plain)


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

    for i in cleartext.lower():
        indx = (key.index(i) + 13) % 26
        result += key[indx]

    return result.lower()


def decrypt(cipher):

    result = ''

    for i in cipher.lower():
        indx = (key.index(i) - 13) % 26
        result += key[indx]

    return result.lower()

def printer(cipher, plain):
    print(cipher)
    print(plain)


def display_message():
    pass


if __name__ == '__main__':
    main()
