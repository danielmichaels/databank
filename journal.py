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
"""


def main():
    header()
    run_event()


def run_event():
    print("[L]ist, [U]pdate, [D]elete, E[x]it")
    '''
    cmd = input('[L]ist, [U]pdate, [D]elete, E[x]it')
    
    '''


def insert():
    print('insert test')
    pass


def update():
    print('update test')
    pass


def delete():
    print('delete test')
    pass


def _datetime():
    pass


def display():
    pass


def _database():
    """ save journal stuff into here?
    maybe make this a class?

    load
    save

    """
    pass


def header():
    print("""
    Welcome to Journal v.01
    """)

if __name__ == '__main__':
    main()
