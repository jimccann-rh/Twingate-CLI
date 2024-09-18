import json
import pandas as pd
import logging
import GenericTransformers

def GetUpdateAsCsv(jsonResults):
    columns = ['ok','error','id','name','hasStatusNotificationsEnabled']
    return GenericTransformers.GetUpdateAsCsvNoNesting(jsonResults,'connectorUpdate',columns)

def GetShowAsCsv(jsonResults):
    columns = ['id', 'name','lastHeartbeatAt','hasStatusNotificationsEnabled','state','remoteNetwork.id','remoteNetwork.name']
    return GenericTransformers.GetShowAsCsvNoNesting(jsonResults,'connector',columns)

def GetListAsCsv(jsonResults):
    #privateIPs
    columns = ['id', 'name','state','hostname','version','publicIP','lastHeartbeatAt','hasStatusNotificationsEnabled']
    return GenericTransformers.GetListAsCsv(jsonResults,columns)

def GetGenTokensAsCsv(jsonResults):
    columns = ['ok', 'error','connectorTokens.accessToken','connectorTokens.refreshToken']
    return GenericTransformers.GetShowAsCsvNoNesting(jsonResults,'connectorGenerateTokens',columns)

def GetCreateAsCsv(jsonResults):
    columns = ['ok', 'error','entity.id', 'entity.name']
    return GenericTransformers.GetShowAsCsvNoNesting(jsonResults,'connectorCreate',columns)