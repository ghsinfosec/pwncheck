#!/usr/bin/env python3

# Heath Stewart | 22 September 2021
# Reference: https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/

from getpass import getpass
import hashlib
import requests
import subprocess
import sys
from time import sleep


# clear the screen
subprocess.call('clear', shell=True)

# banner
print("-" * 51)
print("                              __              __  ")
print("    ____ _      ______  _____/ /_  ___  _____/ /__")
print("   / __ \ | /| / / __ \/ ___/ __ \/ _ \/ ___/ //_/")
print("  / /_/ / |/ |/ / / / / /__/ / / /  __/ /__/ ,<   ")
print(" / .___/|__/|__/_/ /_/\___/_/ /_/\___/\___/_/|_|  ")
print("/_/                                               ")
print("                   [ghsinfosec]                   ")
print("-" * 51)
print("\nEnter a password to check against known data breaches.")

# sleep 1 second and get the password
sleep(1)
password = getpass(prompt='Password: ', stream=None)

# color scheme for breach notifications - red = warning, green = safe
red = '\033[31m'
green = '\033[32m'


def pwncheck(password):
    # get the sha1 hash of submitted pw
    sha1 = hashlib.sha1(password.encode('utf-8'))
    pw_hash = sha1.hexdigest().upper()  # convert to upper case
    print(f'SHA1 Hash of entered password: {pw_hash}')
    prefix = pw_hash[0:5]               # necessary for the api, ref above

    url = f'https://api.pwnedpasswords.com/range/{prefix}'

    response = requests.get(url).content.decode('utf-8') # store the response in utf-8 format
    
    # create a dictionary to store the key/value pairs of returned hashes
    hash_data = dict(i.split(':') for i in response.split('\r\n'))

    # include the prefix to store the full pw hash
    hash_data = dict((prefix + key, value) for (key, value) in hash_data.items())
    
    # check for the pw hash in the dictionary to find a match
    for k,v in hash_data.items():
        # match found, pw is compromised
        if k == pw_hash:
            print(f'{red} [!!] Password seen {v} times in data breaches! Do NOT use this password! [!!]')
            break

    # no match found, pw is good for now
    if pw_hash != k:
        print(f'{green} The password you entered has not been found in any data breach!')
    

pwncheck(password)

