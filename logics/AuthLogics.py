import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')
import DataUtils
import StdResponses
import AuthResponses
import logging
import StdAPIUtils

def login(apikey,url,sessionname):

    FULLURL = url

    DataUtils.StoreAuthToken(apikey,sessionname)
    DataUtils.StoreUrl(url,sessionname)
    print("Token Stored in session: "+sessionname)

def logout(sessionname):
    DataUtils.DeleteSessionFiles(sessionname)
    print("Session deleted: "+sessionname)

def listSessions():
    SessionList,IsError = DataUtils.listSessions()
    if(IsError):
        print("Error retrieving session list.")
    else:
        print(SessionList)