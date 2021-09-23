# pwncheck
### Breached password checker
pwncheck is a tool that you will check the status of any passwords you have or plan to use. It leverages the [HaveIBeenPwned](https://haveibeenpwned.com) pwndpasswords api to check the SHA1 hash of a provided password.

If pwncheck discovers the submitted password in the pwnedpasswords list, it will display a red text letting you know how many times that password was seen in data breaches. Otherwise it will display a green text letting you know that the password you entered has not been breached.....yet...

## Requirements
requests

To install the python requests library:
```bash
pip3 install requests
```

## Installation
```bash
git clone https://github.com/ghsinfosec/pwncheck.git
```

To add a symbolic link and run it from anywhere type:
```bash
sudo ln -s $(pwd)/pwncheck.py /usr/local/bin/pwncheck
```

## Usage
pwncheck takes no arguments. Run it from the commandline and enter a password when prompted.
```bash
pwncheck
```

Example using 'password' as the password:
```bash
---------------------------------------------------
                              __              __  
    ____ _      ______  _____/ /_  ___  _____/ /__
   / __ \ | /| / / __ \/ ___/ __ \/ _ \/ ___/ //_/
  / /_/ / |/ |/ / / / / /__/ / / /  __/ /__/ ,<   
 / .___/|__/|__/_/ /_/\___/_/ /_/\___/\___/_/|_|  
/_/                                               
                   [ghsinfosec]                   
---------------------------------------------------

Enter a password to check against known data breaches.
Password: 
 [!!] The password you entered has been seen 3861493 times in data breaches! Do NOT use this password! [!!]

```
