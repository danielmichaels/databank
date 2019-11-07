#!/usr/bin/env python3
import datetime
import os
import pwd

""" This is a replication of unix List Structure tool. """


def main():
    banner()
    command = cli()
    list_directory = ListStructure()
    printer(command, list_directory)


def cli():
    """ Where user inputs ls commands """
    command = input(">> ")
    # command = 'ls' # testing
    # command = 'ls -l' # testing
    # command = 'ls -la'  # testing
    return command


def printer(command, list_directory):
    """ Return the ls command"""

    if command == "ls":
        print(list_directory.ls)

    elif command == "ls -l":
        list_directory.ls_l

    elif command == "ls -la":
        list_directory.ls_la

    else:
        print("Command not recognised, did you mean 'ls'?")


class ListStructure:
    """ Class that creates the ls, ls -l and ls -la methods. """

    def __init__(self):
        """ The args search through the current directory for files. """
        self.list_l = [i for i in os.listdir() if not i.startswith(".")]
        self.list_la = [i for i in os.listdir()]

    @property
    def ls(self):
        """ Unix most basic implementation of the 'ls' command. """
        return self.list_l

    @property
    def ls_l(self):
        """ Outputs 'ls -l' unix tool. """
        info = dict()
        ls = self.list_l

        for i in ls:
            info["permissions"] = (oct(os.lstat(i).st_mode))[-4:]
            info["size"] = os.path.getsize(i)
            info["time"] = ListStructure.convert_time(i)
            info["uid"] = pwd.getpwuid(os.stat(i).st_uid).pw_name
            info["gid"] = os.getgid()  # find the gid name rather than number.
            info["file"] = i
            print(
                f"{info['permissions']}\t{info['uid']} {info['gid']}\t"
                f"{info['size']}B\t{info['time']}\t {i}"
            )

        # return info

    @property
    def ls_la(self):
        info = dict()
        ls = self.list_la

        for i in ls:
            info["permissions"] = (oct(os.lstat(i).st_mode))[-4:]
            info["size"] = os.path.getsize(i)
            info["time"] = ListStructure.convert_time(i)
            info["uid"] = pwd.getpwuid(os.stat(i).st_uid).pw_name
            info["gid"] = os.getgid()  # find the gid name rather than number.
            info["file"] = i
            print(
                f"{info['permissions']}\t{info['uid']} {info['gid']}\t"
                f"{info['size']}B\t{info['time']}\t {i}"
            )

    @staticmethod
    def convert_time(file):
        """ Helper function for time conversion. """
        t = os.path.getmtime(file)
        utcts = datetime.datetime.utcfromtimestamp(t)
        fmt = "%-d %b %H:%M"

        return utcts.strftime(fmt)


def banner():
    print()
    print("#" * 40)
    print("\t\tList Directory Tool")
    print("#" * 40)


if __name__ == "__main__":
    main()
