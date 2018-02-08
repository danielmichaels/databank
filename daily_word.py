#!/usr/bin/env python3

import sqlite3
from pprint import pprint


def main():
    import_words()


def import_words():
    """Import the words.txt"""
    word_list = list()
    with open('words.txt', 'r') as fin:
        for line in fin.readlines():
            word_list.append(line)

    word_list = clean_text(word_list)

    word_list = [word for word in word_list if len(word) != 1]

    for idx, words in enumerate(word_list):
        if len(words) != 1:
            print("[{}] - {} : length == {}".format(idx, words, len(words)))

    words = [x[0] for x in word_list]
    words_upper = [x.upper() for x in words]


def clean_text(text: list):
    caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if not text:
        return text
    txt = [txt.strip('').strip('\n') for txt in text]  # rm '' & newlines
    txt = list(filter(None, txt))  # remove null strings
    # txt = filter(len(1), txt)

    # if txt[0]

    return txt


if __name__ == '__main__':
    main()
