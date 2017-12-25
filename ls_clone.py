#!/usr/bin/env python3
import datetime
import os

""" What does 'ls' do?
A very basic implementation of the unix 'ls' tool.

BASIC: lists directory --> it needs a start point --> prints file names
ADV: prints, rwx, size, last edited, owner, group

"""


def main():
    banner()
    command = cli()
    printer(command)


def cli():
    """ Where user inputs ls commands """
    command = input('>> ')
    return command


def printer(command):
    """ Return the ls command"""
    # ls = 'ls'
    # ls_l = 'ls -l'
    # ls_la = 'ls -la'

    if command == 'ls':
        ls()

    elif command == 'ls -l':
        ls_l()

    elif command == 'ls -la':
        ls_la()

    else:
        print('Command not recognised, did you mean \'ls\'?')


def ls():
    """ Unix most basic implementation of the 'ls' command. """
    l = [print(i) for i in os.listdir()]
    return l


def ls_l():
    """ Outputs 'ls -l' unix tool. """
    ls = [i for i in os.listdir()]
    for i in ls:
        permissions = (oct(os.lstat(i).st_mode))[-4:]
        size = os.path.getsize(i)
        time = convert_time(i)
        uid = os.getuid()
        # pwd.getpwuid(os.stat(i).st_uid).pw_name
        # this will return user name rather than number.
        gid = os.getgid()
        print(f'{permissions}\t{uid} {gid}\t{size}B\t{time}\t {i}')

    pass


def ls_la():
    pass


def convert_time(file):
    """ Helper function for time conversion. """

    t = os.path.getmtime(file)
    utcts = datetime.datetime.utcfromtimestamp(t)
    fmt = '%-d %b %H:%M'

    return utcts.strftime(fmt)

    # return datetime.datetime.fromtimestamp(t)


def banner():
    print()
    print('#' * 40)
    print('\t\tList Directory Tool')
    print('#' * 40)


if __name__ == '__main__':
    main()
