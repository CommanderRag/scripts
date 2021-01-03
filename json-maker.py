import json
import base64
import requests
import os

owner = "CommanderRag"
repo = "scripts"
token = os.environ.get("github_token")
print(token)


lv = input("Enter latest version:")
url = "https://raw.githubusercontent.com/CommanderRag/scripts/master/json-content.json"
releaseNotes = input("Enter release notes:")
arr = releaseNotes.split(",")
json_var = {"latestVersion":lv, "url":url,
                   "releaseNotes":arr}

json2 = json.dumps(json_var)
print(json2)

bytes = json2.encode('ascii')
base64 = base64.b64encode(bytes)

print("\n")

commit = input("Enter commit name:")

post_url = "https://api.github.com/repos/CommanderRag/scripts/contents/json-content.json"

headers = {"Authorization":os.environ.get("github_token")}

data_json = {"message":commit,"content":base64.decode("utf-8")}
data = json.dumps(data_json)


def create():
  response = requests.put(post_url,headers=headers,data=data)
  if(response.status_code<400):
    print(response.status_code)
    print(response.json)
  elif(response.status_code==422):
    url = "https://api.github.com/repos/CommanderRag/scripts/contents/json-content.json"
    request = requests.get(url,headers=headers)
    sha = request.text
    sha = json.loads(sha)
    sha = sha["sha"]
    print("\n")
    dict_sha = {"message":commit,"content":base64.decode('utf-8'),"sha":sha}
    dict_sha = json.dumps(dict_sha)
    request_sha = requests.put(post_url,headers=headers,data=dict_sha)
    print(request_sha.status_code)
    if(request_sha.status_code >=400):
        print(request_sha.text)
  else:
    print("Error")
    print("\n")
    print(response.json)

create()
