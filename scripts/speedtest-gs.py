#!/usr/bin/env python3
###################
import pygsheets
import speedtest
import datetime

# global VAR
DATE = datetime.datetime.now().strftime('%d/%m/%y %H:%M')


def get_credentials():
    """Function to check for valid OAuth access tokens."""
    gc = pygsheets.authorize(outh_file="client_secret.json")
    return gc


def submit_into_spreadsheet(download, upload, ping):
    """Function to submit speedtest result."""
    gc = get_credentials()

    speedtest = gc.open('Speedtest')
    sheet = speedtest.worksheet('title', 'VPN')  # VPN; uncomment as req
    # sheet = speedtest.worksheet('title','Clear') # Clear; uncomment as req
    data = [DATE, download, upload, ping]

    sheet.append_table(values=data)  # uncomment for clear


def main():
    # Check for proper credentials
    print("Checking OAuth validity...")
    get_credentials()

    # Run speedtest and store output
    print("Starting speed test...")
    spdtest = speedtest.Speedtest()
    spdtest.get_best_server()
    download = '{:.2f}'.format(spdtest.download() / 1000.0 / 1000.0)
    upload = '{:.2f}'.format(spdtest.upload() / 1000000)
    ping = float(spdtest.results.ping)
    print("Starting speed finished!")

    # Write to spreadsheet
    print("Writing to spreadsheet...")
    submit_into_spreadsheet(download, upload, ping)
    print("Successfuly written to spreadsheet!")


if __name__ == "__main__":
    main()
