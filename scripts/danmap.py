#!/usr/bin/env python
import datetime
import time
import socket
import sys


def main():
    cli()


def connect_scan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        status_code = sock.connect_ex((host, port))
        if status_code == 0:
            return status_code

        sock.close()

    except Exception:
        pass


def cli():
    host = "scanme.nmap.org"
    host_ip = socket.gethostbyname(host)
    closed_ports = []
    open_ports = []

    start = time.time()
    for port in range(0, 104):
        try:
            resp = connect_scan(host, port)
            if resp == 0:
                open_ports.append(port)

            if resp == 1:
                closed_ports.append(port)

        except KeyboardInterrupt:
            print("[!!] Application Stopping...")
            print("[!!] Keyboard Interrupt!")
            sys.exit(1)
    stop = time.time()
    total_time = stop - start
    printer(host, host_ip, closed_ports, open_ports, total_time)


def printer(host, host_ip, closed_ports, open_ports, total_time):
    print(f"Starting DaNmap 1.0 at {datetime.datetime.now()}")
    print(f"DaNmap report for {host} ({host_ip})")
    print(f"Not shown: {len(closed_ports)} Ports Closed")
    print()

    print("PORT\tSTATE\tSERVICE")
    for port in open_ports:
        print(f"{port}")

    print()
    print(f"Scan completed in {total_time} seconds")


if __name__ == "__main__":
    main()
