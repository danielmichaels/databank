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
    """
    Asks user for message to encrypt.

    :return: Plaintext message for encryption.
    """
    message = input('Enter the message: ')

    return message


def encrypt(cleartext):
    """
    Encrypts the message using ROT13.

    :param cleartext: Takes message arg.
    :return: encrypted message in lowercase.
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
    """
    Decrypts the message

    :param cipher: Takes cipher text
    :return: decrypted plaintext message.
    """
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


if __name__ == '__main__':
    main()
