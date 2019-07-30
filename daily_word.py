#!/usr/bin/env python3

import sqlite3
from pprint import pprint


def main():
    file = import_words()
    etl(file)


def import_words():
    """Import the words.txt"""
    word_list = list()
    with open('words.txt', 'r') as fin:
        for line in fin.readlines():
            word_list.append(line)
    return word_list

def etl(word_list):
    """Take in the word list and remove redundancies and cleanup text."""

    word_list = clean_text(word_list) # clean up the text
    word_list = [word for word in word_list if len(word) != 1]
    rm_non_letters = [word[0] for word in word_list if not ]

    # remove non-definition words e.g headings.

    for idx, words in enumerate(word_list):
        print("[{}] - {} : length == {}".format(idx, words, len(words)))



def clean_text(text: list):
    if not text:
        return text
    txt = [txt.strip('').strip('\n') for txt in text]  # rm '' & newlines
    txt = list(filter(None, txt))  # remove null strings
    return txt


if __name__ == '__main__':
    main()
