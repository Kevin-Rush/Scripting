import json
import requests

tenants = {
"m0121": {"customer_name" : "BIG", "client_id" : "871202a3-1312-3bf1-980f-28f34c16713d", "client_secret" : "16325960-baa5-33a9-9b3d-a737eeef3eeb", "tenant_tech_name" : "a3b2d07a5", "provider_account" : "avrfme", "application" : "m0121tmn"},
"m0122": {"customer_name" : "NOVA", "client_id" : "2a54e735-f308-31b0-a9ed-1a2ea43f5993", "client_secret" : "25eaa47f-667e-3c88-a6f8-e83c48595822", "tenant_tech_name" : "a507858e1", "provider_account" : "avrfme", "application" : "m0122tmn"},
"m0123": {"customer_name" : "ABC", "client_id" : "d31b4937-780d-38a1-bd3d-a1bdb55c3444", "client_secret" : "9b2811f9-2ad9-321f-a8bd-508d4dd2e9fd", "tenant_tech_name" : "a32f96f5d", "provider_account" : "avrfme", "application" : "m0123tmn"},
"m0124": {"customer_name" : "ABC", "client_id" : "d2fbc85a-7669-3037-8b78-771c329faa89", "client_secret" : "1f2806b6-8523-3824-812f-ce0728ce1f70", "tenant_tech_name" : "afd8ca932", "provider_account" : "avrfme", "application" : "m0124tmn"},
"m0125": {"customer_name" : "B.I.", "client_id" : "0dc2d589-009e-387c-b6e0-9e5d7fb2892b", "client_secret" : "afaa2da9-ed24-33b7-af50-5dd49ad517b0", "tenant_tech_name" : "a740584cb", "provider_account" : "avrfme", "application" : "m0125tmn"},
"m0126": {"customer_name" : "DSP", "client_id" : "c82f8e14-c1d9-3a80-823c-08858eb358e7", "client_secret" : "c4021631-1a08-326c-b28d-61d15d7c74f7", "tenant_tech_name" : "a7beebf5c", "provider_account" : "avrfme", "application" : "m0126tmn"},
"m0128": {"customer_name" : "DRL", "client_id" : "7638e836-ecb7-364f-b809-34f7fe4dfb84", "client_secret" : "52b7dbcb-c201-3603-a064-d70fbdb00bd5", "tenant_tech_name" : "ac97cfcfa", "provider_account" : "avrfme", "application" : "m0128tmn"},
"m0129": {"customer_name" : "BAYER", "client_id" : "cf332dc5-e309-357d-923f-234e647c44a5", "client_secret" : "c286cdba-5584-3f15-a3ad-02a9e59514a8", "tenant_tech_name" : "a6bb7df7f", "provider_account" : "avrfme", "application" : "m0129tmn"},
"m0130": {"customer_name" : "AZ", "client_id" : "831447da-2ec6-3a08-b9ed-cde5eaea0368", "client_secret" : "1f2957b8-2066-3405-be39-b50de253109f", "tenant_tech_name" : "a85b9be53", "provider_account" : "avrfme", "application" : "m0130tmn"},
"m0131": {"customer_name" : "ALVG", "client_id" : "016f1070-48d3-3a35-9a0f-6c2f13df0655", "client_secret" : "923e5976-328e-3cb2-92a9-f9c44011fab8", "tenant_tech_name" : "ab543e794", "provider_account" : "avrfme", "application" : "m0131tmn"},
"m0134": {"customer_name" : "INTERNAL_DEV", "client_id" : "2e650d56-1d42-3581-aac3-3bf0bab76454", "client_secret" : "7d64077b-d8af-325d-92bb-a96b61dd0c22", "tenant_tech_name" : "a9d68ab03", "provider_account" : "avrfme", "application" : "m0134tmn"},
"m0135": {"customer_name" : "INTERNAL_EUHUB", "client_id" : "226be683-9977-3664-849a-93d5f6ee2118", "client_secret" : "532f3515-0838-3a37-b4f6-bf68a3a350bc", "tenant_tech_name" : "a7e57649b", "provider_account" : "avrfme", "application" : "m0135tmn"},
"m0138": {"customer_name" : "GSK", "client_id" : "962ba528-5d14-3dae-94ef-c04a18f61987", "client_secret" : "826b3455-9aa5-343f-bc61-854be576a2f8", "tenant_tech_name" : "a4a91e770", "provider_account" : "avrfme", "application" : "m0138tmn"},
"m0522": {"customer_name" : "J&J", "client_id" : "9f247482-c6e8-3efa-acd4-c62af14fec16", "client_secret" : "b39562f8-3a20-3a66-8b88-f7b886a23195", "tenant_tech_name" : "d3adb5224", "provider_account" : "avpfme", "application" : "m0522tmn"},
"m0523": {"customer_name" : "MERCK", "client_id" : "659d635c-7355-3abe-b69d-2d646175fdf9", "client_secret" : "4708802c-1955-34e6-bf79-8fe3632779df", "tenant_tech_name" : "d103b7232", "provider_account" : "avpfme", "application" : "m0523tmn"},
"m0525": {"customer_name" : "VAL", "client_id" : "917dab91-40b2-3d3c-9a21-8c5a8c320b93", "client_secret" : "dd79fa67-c7b3-3f97-a979-3efa46b0099a", "tenant_tech_name" : "d18893b11", "provider_account" : "avpfme", "application" : "m0525tmn"},
"m0526": {"customer_name" : "NEST", "client_id" : "d26dd486-d401-373d-bf5d-03d9a1c8d12f", "client_secret" : "7b870683-13b9-3718-98dc-3b3d3997abee", "tenant_tech_name" : "d94e1d5ac", "provider_account" : "avpfme", "application" : "m0526tmn"},
"r0121": {"customer_name" : "BIG", "client_id" : "699b4139-8c5c-3b51-9e70-3ec0fb2a26f2", "client_secret" : "183d8051-374c-3dd8-b4d4-123a4ec5125b", "tenant_tech_name" : "aa224561f", "provider_account" : "avrgfmp", "application" : "r0121tmn"},
"r0122": {"customer_name" : "NOVA", "client_id" : "ac3f3768-0b85-39e1-8915-3d89a8f6450b", "client_secret" : "9d32f060-4e7c-32d5-a15e-2a1b39700499", "tenant_tech_name" : "a277f6877", "provider_account" : "avrgfmp", "application" : "r0122tmn"},
"r0125": {"customer_name" : "B.I.", "client_id" : "00879cd8-1f57-3238-9159-3a0a29c307a3", "client_secret" : "ccdcd0f7-bc35-385f-bbb0-e520bfcf64bf", "tenant_tech_name" : "a14c20d2e", "provider_account" : "avrgfmp", "application" : "r0125tmn"},
"r0126": {"customer_name" : "DSP", "client_id" : "5597b3d2-45f6-3069-b8f8-63704ffc0784", "client_secret" : "bbf8f1ea-62e1-3c45-bc13-40b11a559865", "tenant_tech_name" : "a95e0de70", "provider_account" : "avrgfmp", "application" : "r0126tmn"},
"r0128": {"customer_name" : "DRL", "client_id" : "3454d0a9-cdd6-3869-9406-ebb796f1cdfa", "client_secret" : "49184d62-1364-3fa9-9d12-d3ba7ece5c53", "tenant_tech_name" : "a41d42b81", "provider_account" : "avrgfmp", "application" : "r0128tmn"},
"r0129": {"customer_name" : "BAYER", "client_id" : "880b9a60-f92e-3620-b6b7-7e74c1ff3b40", "client_secret" : "8f7e9153-4650-3d45-aaff-50d14aae2e86", "tenant_tech_name" : "af5d34adc", "provider_account" : "avrgfmp", "application" : "r0129tmn"},
"r0130": {"customer_name" : "AZ", "client_id" : "0456433d-774e-3099-bbd2-7e5e52f9c43f", "client_secret" : "74ab9c35-b092-3bdf-9dfc-3946601dfeec", "tenant_tech_name" : "a62019354", "provider_account" : "avrgfmp", "application" : "r0130tmn"},
"r0131": {"customer_name" : "ALVG", "client_id" : "c083d10d-037a-330a-a8e7-1aca25103cb7", "client_secret" : "2a58ae2b-e402-371d-9594-9bc0102b027d", "tenant_tech_name" : "aac11bb39", "provider_account" : "avrgfmp", "application" : "r0131tmn"},
"r0134": {"customer_name" : "INTERNAL_QA", "client_id" : "2c353c45-97f1-3364-a614-dbe1628b1e54", "client_secret" : "be26d7f3-7466-3adb-9d6c-bb544fc69ead", "tenant_tech_name" : "a7366ca2f", "provider_account" : "avrgfmp", "application" : "r0134tmn"},
"r0135": {"customer_name" : "INTERNAL_TEST", "client_id" : "6f35a46a-d3b1-3a34-a229-bf5a92f67d47", "client_secret" : "dc66038a-7c1b-3546-85c8-ce15cfca8908", "tenant_tech_name" : "ae4f64f31", "provider_account" : "avrgfmp", "application" : "r0135tmn"},
"r0136": {"customer_name" : "INTERNAL_PLAY", "client_id" : "5e737ca7-9afa-392a-95eb-ca13853178fe", "client_secret" : "ab51f0b6-42bc-35d3-8f3e-1e9cc51a27a4", "tenant_tech_name" : "af73dd9d7", "provider_account" : "avrgfmp", "application" : "r0136tmn"},
"r0138": {"customer_name" : "GSK", "client_id" : "29661bea-0cd2-3cc8-a9de-7509796b8ba6", "client_secret" : "0dfb9345-a80a-3bf6-86e9-3fcb80da3706", "tenant_tech_name" : "a3d96d7e6", "provider_account" : "avrgfmp", "application" : "r0138tmn"},
"r0521": {"customer_name" : "ABC", "client_id" : "742ec662-30fe-3447-86a0-aa0d8e010954", "client_secret" : "5f07a095-68be-3500-853d-9a197cd3a519", "tenant_tech_name" : "d380cefa1", "provider_account" : "avpgfmp", "application" : "r0521tmn"},
"r0522": {"customer_name" : "J&J", "client_id" : "9635d305-8b24-3aeb-9481-5a4d0a33f441", "client_secret" : "4ca79e78-55b6-3843-866b-a7509b7d0a77", "tenant_tech_name" : "dfb1e695e", "provider_account" : "avpgfmp", "application" : "r0522tmn"},
"r0523": {"customer_name" : "MERCK", "client_id" : "55806d1a-59ff-3772-a257-2e10dcb937fc", "client_secret" : "0a87e7a5-ff86-3af4-a6f2-b4d730486823", "tenant_tech_name" : "d673c42a4", "provider_account" : "avpgfmp", "application" : "r0523tmn"},
"r0525": {"customer_name" : "VAL", "client_id" : "7b6da63d-1ada-3916-bba0-2af1144b1c22", "client_secret" : "e66b2410-16e6-313d-ac84-7bae585e02ef", "tenant_tech_name" : "d86edaeb2", "provider_account" : "avpgfmp", "application" : "r0525tmn"},
"r0526": {"customer_name" : "NEST", "client_id" : "c0693e59-f3cd-3f89-b4b9-7a2f285bf54a", "client_secret" : "e71331a8-258e-3808-b269-b7afb16f7740", "tenant_tech_name" : "d045ec83d", "provider_account" : "avpgfmp", "application" : "r0526tmn"}
}


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
"""
bToken=getToken()
r0136_accountName = "af73dd9d7"
r0136_appName = "r0136tmn"
r0136_providerAccount = "avrgfmp"

groups = getGroups(r0136_accountName, bToken)
print(groups)

printAll(groups["groups"])#print - ["groups"][i]["name"]
roles = getRoles(r0136_accountName, r0136_appName, r0136_providerAccount, bToken)
"""

print(tenants["m0121"])