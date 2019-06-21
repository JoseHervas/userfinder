import requests
import sys
import os
import urllib3
import re
from lxml import html

NOT_FOUND_PATTERNS = ["doesn't exist", "does not exist", "no such user", "not found", "could not be found"]

if len(sys.argv) < 2:
    print("Usage: {} <username>".format(sys.argv[0]))
    exit(1)

# Disabling insecure request warnings for HTTPS sites
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get some pretty colors for *NIX/Powershell
class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def check_username(user):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
    }

    print(bcolors.HEADER + "[*] Searching on social medias" + bcolors.ENDC)
    with open("./sites/social.txt", "r") as sites:
        for site in sites:
            try:
                r = requests.get(site.format(user).rstrip(), headers=headers, verify=False, timeout=10)
                if r.status_code == 200:
                    if not any(p in str(r.content).lower() for p in NOT_FOUND_PATTERNS):
                        print(bcolors.WARNING + "[+] Profile found: " + bcolors.ENDC + r.url)
            except requests.exceptions.ReadTimeout:
                continue



if __name__ == "__main__":

    check_username(sys.argv[1])