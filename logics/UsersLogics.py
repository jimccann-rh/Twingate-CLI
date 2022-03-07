import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './transformers')
import DataUtils
import GenericTransformers
import StdResponses
import StdAPIUtils

def get_user_list_resources(sessionname,token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"

    Body = """
            {
          users(after: null, first:100) {
            edges {
              node {
                id
               	avatarUrl
                state
                email
                state
                isAdmin
                lastName
                firstName
                createdAt
                updatedAt
              }
            }
            pageInfo {
              startCursor
              hasNextPage
            }
          }
        }
    """

    return True,api_call_type,Headers,Body


def user_list(outputFormat,sessionname):
    StdAPIUtils.generic_api_call_handler(outputFormat,sessionname,get_user_list_resources,{},GenericTransformers.GetListAsCsv,'users')
