import csv
import subprocess
import os
import random
import string
import re
import secrets
import json
import ipaddress

# Load the JSON file.
with open("cdata.json", "r") as f:
      data = json.load(f)


#Twingate-CLI

logintenat = os.environ["TG_TENANT"]
loginapi = os.environ["TG_API"]


#loginoutput = subprocess.check_output('python3 ./tgcli.py auth login -t ' + logintenat + ' -a ' + loginapi, shell=True)
#session = loginoutput.decode("utf-8").split(":")[1].strip()
#print(session)

for x in data:
#    print(x["id"])
#    print(x["vlanNumber"])
#    print(x["subnets"][0]["networkIdentifier"])
    ip4ni = x["subnets"][0]["networkIdentifier"]
    ip4nm = x["subnets"][0]["netmask"]

    ip4 = ipaddress.IPv4Network((ip4ni,ip4nm))
    #ip4 = ipaddress.IPv4Network((0,'255.255.255.0'))
#    print(ip4.prefixlen)
#    print(ip4.with_prefixlen)


    segmentname = "IBMC-devqe segment-" + str(ip4ni)
    #segmentname = "IBMC-devqe segment-" + str(ip4.prefixlen)
    networkrange = ip4.with_prefixlen
    print(segmentname)
    print(networkrange)
    command = ["python3", "./tgcli.py", "-s", session, "resource", "create", "-a", networkrange, "-n", segmentname, "-r", "UmVtb3RlTmV0d29yazozNzc0Mg==", "-g", "R3JvdXA6MTA5MDkw"]
    subprocess.call(command)

command3 = ["python3", "./tgcli.py", "auth", "logout", "-s", session]
subprocess.call(command3)
