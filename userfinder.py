import sys
import requests
import html
import urllib3

if len(sys.argv) < 2:
    print("Usage: {} <username>".format(sys.argv[0]))
    exit(1)

# Disabling insecure request warnings for HTTPS sites
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

print(bcolors.OKGREEN + """
 _   _               _____ _           _
| | | |___  ___ _ __|  ___(_)_ __   __| | ___ _ __
| | | / __|/ _ \ '__| |_  | | '_ \ / _` |/ _ \ '__|
| |_| \__ \  __/ |  |  _| | | | | | (_| |  __/ |
 \___/|___/\___|_|  |_|   |_|_| |_|\__,_|\___|_|
""" + "\n"
+ bcolors.ENDC + "by tr4cefl0w\n")

def check_username(user):

    not_found_msg = ["doesn&#8217;t&nbsp;exist", "doesn't exist", "no such user", 
                    "not found", "could not be found", "https://pastebin.com/index", "user not found",
                    "usererror-404"]


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
    }

    print(bcolors.OKBLUE + "[*] Searching on social medias" + bcolors.ENDC)
    with open("./sites/social.txt", "r") as sites:
        for site in sites:
            try:
                r = requests.get(site.format(sys.argv[1]).rstrip(), headers=headers)
                if r.status_code == 200:
                    found = [p in r.text.lower() for p in not_found_msg]
                    if True not in found:
                        print(bcolors.WARNING + "[+] Profile found: " + bcolors.ENDC + r.url)
            except Exception as e:
                print(e)
                continue



if __name__ == "__main__":

    check_username(sys.argv[1])
