import json
import requests

def getToken():
    post_endpoint="https://api.hana.ondemand.com/oauth2/apitoken/v1?grant_type=client_credentials"

    post_req = requests.post(post_endpoint, auth=('5e737ca7-9afa-392a-95eb-ca13853178fe', 'ab51f0b6-42bc-35d3-8f3e-1e9cc51a27a4'))
    data = json.loads(post_req.text)

    print(post_req.text+"\n")

    bearer_token = 'Bearer '+data["access_token"]
    header={'Authorization':bearer_token}
    
    print(bearer_token+"\n")

    return header

def getGroups(accountName, bToken):
    get_endpoint="https://api.hana.ondemand.com/authorization/v1/accounts/"+accountName+"/groups"

    get_req = requests.get(get_endpoint, headers=bToken)
    print ("Groups status_code: " +str(get_req.status_code)+"\n")
    groups = json.loads(get_req.text)
    return groups

def getRoles (accountName, appName, providerAccount, bToken):
    get_endpoint="https://api.hana.ondemand.com/authorization/v1/accounts/"+accountName+"/apps/"+appName+"/roles?providerAccount="+providerAccount
    get_req = requests.get(get_endpoint, headers=bToken)
    print ("Roles status_code: " +str(get_req.status_code)+"\n")

    roles = json.loads(get_req.text)
    list_roles = []
    
    for i in range(len(roles["roles"])):
        print(roles["roles"][i]["name"])
        list_roles.append(roles["roles"][i]["name"])
    
    return list_roles

def printAll(list):
    for i in list:
        print(i["name"])
    print()

bToken=getToken()
r0136_accountName = "af73dd9d7"
r0136_appName = "r0136tmn"
r0136_providerAccount = "avrgfmp"

groups = getGroups(r0136_accountName, bToken)
print(groups)
printAll(groups["groups"])#print - ["groups"][i]["name"]

roles = getRoles(r0136_accountName, r0136_appName, r0136_providerAccount, bToken)
print(roles)

#printAll(groups["groups"])
