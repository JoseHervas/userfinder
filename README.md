# UserFinder
## A better userrecon
I've been using userrecon for a while but was tired of wasting time with all the  false-positives it was returning and the invalid URLs. The tool is barely maintained and the author not reacting to all the issues opened on GitHub.

So I create UserFinder, which as you will see, is very simple and contains no false-positives (for now).

## Usage
python3 userfinder.py <username>

## Example
```
$ python3 userfinder.py tr4cefl0w

 _   _               _____ _           _
| | | |___  ___ _ __|  ___(_)_ __   __| | ___ _ __
| | | / __|/ _ \ '__| |_  | | '_ \ / _` |/ _ \ '__|
| |_| \__ \  __/ |  |  _| | | | | | (_| |  __/ |
 \___/|___/\___|_|  |_|   |_|_| |_|\__,_|\___|_|

by tr4cefl0w

[*] Searching...
[+] Profile found: https://twitter.com/tr4cefl0w
[+] Profile found: https://www.reddit.com/user/tr4cefl0w
[+] Profile found: https://tr4cefl0w.wordpress.com/
[+] Profile found: https://github.com/tr4cefl0w
[+] Profile found: https://en.gravatar.com/tr4cefl0w
```

