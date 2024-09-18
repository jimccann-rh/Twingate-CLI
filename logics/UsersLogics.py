import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './transformers')
import DataUtils
import UsersTransformers
import GenericTransformers
import StdResponses
import StdAPIUtils

def get_user_change_state_resource(token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"
    variables = {"userID":JsonData['itemid'],"state":JsonData['state']}

    Body = """
     mutation
    userDetailsUpdate($userID:ID!,$state:UserStateUpdateInput!){
    userDetailsUpdate(id:$userID,state:$state) {
        ok
      error
        entity {
               id
                state
                email
                state
                role
                lastName
                firstName
                createdAt
                updatedAt
         }
      }
  }
    """

    return True,api_call_type,Headers,Body,variables

def get_user_create_resource(token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"
    variables = {"email":JsonData['email'],"firstname":JsonData['firstname'],"lastname":JsonData['lastname'],"userRole":JsonData['userRole'],"shouldsendinvite":JsonData['shouldsendinvite']}

    Body = """
     mutation
    UserCreate($email: String!,$firstname: String!,$lastname: String!,$userRole:UserRole!,$shouldsendinvite:Boolean!){
  userCreate(email:$email,firstName:$firstname,lastName:$lastname,role:$userRole,shouldSendInvite:$shouldsendinvite) {
        ok
      error
        entity {
               id
                state
                email
                state
                role
                lastName
                firstName
                createdAt
                updatedAt
         }
      }
  }
    """

    return True,api_call_type,Headers,Body,variables

def get_user_delete_resource(token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"
    variables = {"itemid":JsonData['itemid']}

    Body = """
     mutation
    userDelete($itemid:ID!){
      userDelete(id:$itemid) {
        ok
        error
      }
  }
    """
    return True,api_call_type,Headers,Body,variables

def get_user_reset_mfa(token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"
    variables = {"itemid":JsonData['itemid']}

    Body = """
     mutation
    userResetMfa($itemid:ID!){
      userResetMfa(id:$itemid) {
        ok
        error
      }
  }
    """
    return True,api_call_type,Headers,Body,variables

def get_user_update_role_resource(token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"
    variables = {"itemid":JsonData['itemid'] ,"userRole":JsonData['userRole']}

    Body = """
    mutation
    updateUserRole($itemid: ID!,$userRole: UserRole!){
    userRoleUpdate(id:$itemid,role:$userRole) {
        ok
      error
        entity {
               id
                state
                email
                state
                role
                lastName
                firstName
                createdAt
                updatedAt
                groups{
                  edges{
                    node{
                      id
                    }
                  }
                }
         }
        
      }
  }

    """

    return True,api_call_type,Headers,Body,variables

def get_user_list_resources(token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"
    variables = { "cursor":JsonData['cursor']}

    Body = """
    query listGroup($cursor: String!)
            {
          users(after: $cursor, first:null) {
            pageInfo {
              endCursor
              hasNextPage
            }
            edges {
              node {
                id
                state
                email
                state
                role
                lastName
                firstName
                createdAt
                updatedAt
                groups{
                  edges{
                    node{
                      id
                    }
                  }
                }
              }
            }

          }
        }
    """

    return True,api_call_type,Headers,Body,variables

def get_user_show_resources(token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"
    variables = {"itemID":JsonData['itemid']}
    Body = """
         query
            getObj($itemID: ID!){
          user(id:$itemID) {
                id
                state
                email
                state
                role
                lastName
                firstName
                createdAt
                updatedAt
                groups{
            edges{
                node{
            id
            name
                }
            }

        }
              }
          }
    """

    return True,api_call_type,Headers,Body,variables

def item_show(outputFormat,sessionname,itemid):
    j = StdAPIUtils.generic_api_call_handler(sessionname,get_user_show_resources,{'itemid':itemid})
    output,r = StdAPIUtils.format_output(j,outputFormat,UsersTransformers.GetShowAsCsv)
    print(output)

def item_list(outputFormat,sessionname):
  ListOfResponses = []
  hasMorePages = True
  Cursor = "0"
  while hasMorePages:
    j = StdAPIUtils.generic_api_call_handler(sessionname,get_user_list_resources,{'cursor':Cursor})
    hasMorePages,Cursor = GenericTransformers.CheckIfMorePages(j,'users')
    #print("DEBUG: Has More pages:"+sthasMorePages)
    ListOfResponses.append(j['data']['users']['edges'])
  
  output,r = StdAPIUtils.format_output(ListOfResponses,outputFormat,UsersTransformers.GetListAsCsv)
  print(output)

def update_role(outputFormat,sessionname,itemid,role):
    j = StdAPIUtils.generic_api_call_handler(sessionname,get_user_update_role_resource,{'itemid':itemid,'userRole':role})
    output,r = StdAPIUtils.format_output(j,outputFormat,UsersTransformers.GetUpdateAsCsv)
    print(output)

def delete_user(outputFormat,sessionname,itemid):
    j = StdAPIUtils.generic_api_call_handler(sessionname,get_user_delete_resource,{'itemid':itemid})
    output,r = StdAPIUtils.format_output(j,outputFormat,UsersTransformers.GetDeleteAsCsv)
    print(output)

def reset_mfa(outputFormat,sessionname,itemid):
    j = StdAPIUtils.generic_api_call_handler(sessionname,get_user_reset_mfa,{'itemid':itemid})
    output,r = StdAPIUtils.format_output(j,outputFormat,UsersTransformers.GetDeleteAsCsv)
    print(output)

def create_user(outputFormat,sessionname,email,firstname,lastname,role,shouldsendinvite):
    j = StdAPIUtils.generic_api_call_handler(sessionname,get_user_create_resource,{'email':email,'firstname':firstname,'lastname':lastname,'userRole':role, 'shouldsendinvite':shouldsendinvite})
    output,r = StdAPIUtils.format_output(j,outputFormat,UsersTransformers.GetCreateAsCsv)
    print(output)

def update_user_state(outputFormat,sessionname,itemid,state):
    j = StdAPIUtils.generic_api_call_handler(sessionname,get_user_change_state_resource,{'itemid':itemid,'state':state})
    output,r = StdAPIUtils.format_output(j,outputFormat,UsersTransformers.GetDetailUpdateAsCsv)
    print(output)
