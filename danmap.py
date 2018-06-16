#!/usr/bin/env python

import socket


def main():
    tcp_scan()


def tcp_scan():
    host = 'localhost'

    for port in range(0, 1024):
        try:
            # print(f'Connecting to {host} on {port}')
            sock = socket.socket()
            sock.connect_ex((host, port))
            banner = sock.recv(1024)

            if banner:
                banner = banner.decode('utf-8')
                print(f"[*] {host}:{port} {banner}")
            sock.close()
        except:
            pass


if __name__ == '__main__':
    main()
