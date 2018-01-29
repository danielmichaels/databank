#!/usr/bin/env python3

""" Simple journal app

things it should do:
-->     text files
-->     dated
-->     insert, update, delete
-->     have seperate databases
-->     print to screen == collective, and individually
-->     numbered? idx, dtg, text
-->     completed check mark?
-->     take args on cli (argparser)
"""


def main():
    header()
    run_event()


def run_event():
    """
    cmd = input('[L]ist, [U]pdate, [D]elete, E[x]it')

    """
    journal_data = []
    cmd = None

    while cmd != 'x':
        cmd = input('[L]ist, [U]pdate, [D]elete, E[x]it ')
        cmd = cmd.lower().rstrip()

        if cmd == 'l':
            display(journal_data)
        elif cmd == 'u':
            insert(journal_data)
        elif cmd == 'x':
            print('...Quiting!')
        else:
            print('Command "{}" not recognised. Please try again'.format(cmd))



def insert(journal_data):
    print('insert test')
    text = input('Write here:\n ')
    journal_data.append(text + '\n')

    pass


def delete():
    print('delete test')
    pass


def _datetime():
    pass


def display(journal_data):
    print('testing display')
    for idx, value in enumerate(journal_data):
        print("[*] ({0})    {1}".format(idx + 1, value.rstrip()))
    pass


def _database():
    """ save journal stuff into here?
    maybe make this a class?

    load
    save

    """
    pass

class JournalActions:
    """ Class that saves, loads and deletes journals"""
    def __init__(self, data):
        self.data = data

    def load(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

def header():
    print("""
    ######################################
    
            Welcome to Journal v.01
            
    ######################################
    """)

if __name__ == '__main__':
    main()
