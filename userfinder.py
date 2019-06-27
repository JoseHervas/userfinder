#!/usr/bin/env python3
import sys
import requests
import urllib3

if len(sys.argv) < 2:
    print("Usage: {} <username>".format(sys.argv[0]))
    exit(1)

# Disabling insecure request warnings for HTTPS sites
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SetColor:

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

print(SetColor.OKGREEN + r"""
 _   _               _____ _           _
| | | |___  ___ _ __|  ___(_)_ __   __| | ___ _ __
| | | / __|/ _ \ '__| |_  | | '_ \ / _` |/ _ \ '__|
| |_| \__ \  __/ |  |  _| | | | | | (_| |  __/ |
 \___/|___/\___|_|  |_|   |_|_| |_|\__,_|\___|_|
""" + "\n" + SetColor.ENDC + "by tr4cefl0w\n")


def check_username(user):

    """
    This function takes the user name as argument and loops through each site in the 'sites.txt'
    file to verify is the user account is valid. This is done by first checking for a 200 status
    code. Then, because some sites can't fucking respect RFC standards by returning 200s on invalid
    requests, we have to exclude some responses by checking if a string from the not_found_msg list
    is present in the response. This removes the possibility of false-positives for the sites
    present in the default list.

    Parameters:
        user (str): username to search

    Example:
        check_username(sys.argv[1])

    """

    not_found_msg = [
        "doesn&#8217;t&nbsp;exist",
        "doesn't exist",
        "no such user",
        "page not found",
        "could not be found",
        "https://pastebin.com/index",
        "user not found",
        "usererror-404",
        "he user id you entered was not found"
    ]

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
        }

    print(SetColor.OKBLUE + "[*] Searching..." + SetColor.ENDC)

    with open("./sites.txt", "r") as sites:
        for site in sites:
            try:
                r = requests.get(site.format(sys.argv[1]).rstrip(), headers=headers, timeout=10)
                if r.status_code == 200:
                    found = [p in r.text.lower() for p in not_found_msg]
                    if True not in found:
                        print(SetColor.WARNING + "[+] Profile found: " + SetColor.ENDC + r.url)
            except requests.exceptions.RequestException as e:
                print(e)
                continue


if __name__ == "__main__":

    check_username(sys.argv[1])
