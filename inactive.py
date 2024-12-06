#!/usr/bin/env python3

import csv
import subprocess
import os
import random
import string
import re
import secrets
import json
import argparse
import time
import datetime


#Twingate-CLI

logintenat = os.environ["TG_TENANT"]
loginapi = os.environ["TG_API"]


loginoutput = subprocess.check_output('python3 ./tgcli.py auth login -t ' + logintenat + ' -a ' + loginapi, shell=True)
session = loginoutput.decode("utf-8").split(":")[1].strip()

with open("user_data.txt", "r") as user_data_file:

    # Skip the header line (optional)
    next(user_data_file)

    for line in user_data_file:
        user_info = line.strip().split(",")
        if user_info[4] != "Pending":
            print(f"User ID: {user_info[0]}")
            print(f"Email: {user_info[1]}")
            print(f"Last Name: {user_info[2]}")
            print(f"First Name: {user_info[3]}")
            print(f"Status: {user_info[4]}")
            print(f"Last Resource Access: {user_info[5]}\n")

            id = user_info[0]
            time.sleep(10) # slow down for api throttle
            removeuser = ["python3", "./tgcli.py", "-s", session, "user", "delete", "-i", id]
            subprocess.call(removeuser)
            print(removeuser)

animals = ['BlueFly', 'BlackEel', 'RedBoa', 'BlackBat', 'BlackBoa', 'OrangeFox', 'OrangeApe', 'GreenApe', 'WhiteApe', 'PurpleElk', 'RedCow', 'GreenFox', 'YellowFox', 'PinkBoa', 'YellowElk', 'PinkFox', 'GreenBoa', 'RedBat', 'PurpleApe', 'OrangeBat', 'YellowEel', 'OrangeYak', 'RedDog', 'PinkEel', 'PurpleBat', 'OrangeElk', 'BlueBoa', 'OrangeEel', 'GreenCat', 'WhiteDog', 'OrangeCat', 'BlueCat', 'YellowCat', 'GreenCow', 'BlackYak', 'RedCat', 'WhiteFox']

# Print the list
#for animal in animals:
#   subprocess.call(["python3", "./tgcli.py", "auth", "logout", "-s", animal])

subprocess.call(["python3", "./tgcli.py", "auth", "logout", "-s", session])


