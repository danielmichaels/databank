#!/usr/bin/env python3
import datetime
import os
import pwd

""" What does 'ls' do?
A very basic implementation of the unix 'ls' tool.

BASIC: lists directory --> it needs a start point --> prints file names
ADV: prints, rwx, size, last edited, owner, group

"""


def main():
    banner()
    command = cli()
    list_directory = ListStructure()
    printer(command, list_directory)


def cli():
    """ Where user inputs ls commands """
    command = input('>> ')
    return command


def printer(command, list_directory):
    """ Return the ls command"""
    # ls = 'ls'
    # ls_l = 'ls -l'
    # ls_la = 'ls -la'

    if command == 'ls':
        print(list_directory.ls())

    elif command == 'ls -l':
        list_directory.ls_l()

    elif command == 'ls -la':
        list_directory.ls_la()

    else:
        print('Command not recognised, did you mean \'ls\'?')


class ListStructure():

    def ls(self):
        """ Unix most basic implementation of the 'ls' command. """
        list_directory = [i for i in os.listdir() if
                          not i.startswith('.')]
        # print(list_directory)

        return list_directory

    def ls_l(self):
        """ Outputs 'ls -l' unix tool. """
        info = dict()

        ls = self.ls()

        for i in ls:
            info['permissions'] = (oct(os.lstat(i).st_mode))[-4:]
            info['size'] =  os.path.getsize(i)
            info['time'] = ListStructure.convert_time(i) # This doesn't look very pythonic...
            # info['uid'] = os.getuid()
            info['uid'] = pwd.getpwuid(os.stat(i).st_uid).pw_name
            # pwd.getpwuid(os.stat(i).st_uid).pw_name
            # this will return user name rather than number.
            info['gid'] = os.getgid()
            print(f"{info['permissions']}\t{info['uid']} {info['gid']}\t"
                  f"{info['size']}B\t{info['time']}\t {i}")

    def ls_la(self):
        pass

    def convert_time(file):
        """ Helper function for time conversion. """

        t = os.path.getmtime(file)
        utcts = datetime.datetime.utcfromtimestamp(t)
        fmt = '%-d %b %H:%M'

        return utcts.strftime(fmt)


def banner():
    print()
    print('#' * 40)
    print('\t\tList Directory Tool')
    print('#' * 40)


if __name__ == '__main__':
    main()
