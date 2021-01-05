import json
import base64
import requests
import dropbox

owner = "CommanderRag"
repo = "scripts"
token = ""

dropbox_token = "ReQEsbMrKtoAAAAAAAAAARPxXAAIx1kvY-4I0jwXLGaRRJUtNuS4lj04SNFiStQP"

def deleteAPKwithCode():
  code = input("Enter code to delete apk:")
  if(code != ""):
    try:
      box = dropbox.Dropbox(dropbox_token)
      box.files_delete("/app-release"+str(code)+".apk")
      print("Deleted previous APK successfully!")
    except Exception as e:
      print("File does not exist!")

deleteAPKwithCode()

lv = input("Enter latest version code:")
url = "https://raw.githubusercontent.com/CommanderRag/scripts/master/json-content.json"
releaseNotes = input("Enter release notes:")
arr = releaseNotes.split(",")
json_var = {"latestVersionCode":lv, "name":"app-release"+lv+".apk",
                   "releaseNotes":arr}

json2 = json.dumps(json_var)
print(json2)

bytes = json2.encode('ascii')
base64_str = base64.b64encode(bytes)

print("\n")


commit = input("Enter commit name:")

post_url = "https://api.github.com/repos/CommanderRag/scripts/contents/content/json-content.json"

headers = {"Authorization":f"token {token}"}

data_json = {"message":commit,"content":base64_str.decode("utf-8")}
data = json.dumps(data_json)


def getsha(url_param):
  sha_request = requests.get(url_param,headers=headers)
  sha_text = sha_request.text
  sha_json = json.loads(sha_text)
  sha = sha_json["sha"]
  return sha

def uploadapk():
  drop = dropbox.Dropbox(dropbox_token)
  file = open('storage/shared/app-release.apk','rb')
  data = file.read()

  try:
      drop.files_upload(data, '/app-release'+lv+'.apk', mute=False)
      print("\n")
      print("Uploaded file successfully!")
      print("\n")
  except Exception as e:
      print(str(e))


def create():
  response = requests.put(post_url,headers=headers,data=data)
  if(response.status_code<400):
    print(response.status_code)
  elif(response.status_code==422):
    url = "https://api.github.com/repos/CommanderRag/scripts/contents/content/json-content.json"
    sha = getsha(url)
    print("\n")
    dict_sha = {"message":commit,"content":base64_str.decode("utf-8"),"sha":sha}
    dict_sha = json.dumps(dict_sha)
    request_sha = requests.put(post_url,headers=headers,data=dict_sha)
    print(request_sha.status_code)
    if(request_sha.status_code >=400):
        print(request_sha.json())
  else:
    print("Error")
    print("\n")
    print(response.json())

  input_apk = input("Upload apk too?(y/n):")
  if(input_apk == "y"):
      uploadapk()
  elif(input_apk == "n"):
      print("Aborting...")
  else:
      print("Invalid input. Aborting...")

  print("\n")
  delete_apk = input("Delete previous apk?(y/n):")
  if(delete_apk == "y"):
      num = int(lv)
      number = num - 1
      deletePreviousAPK(number)
  elif(delete_apk == "n"):
      print("Aborting...")
  else:
      print("Invalid input. Aborting...")
create()


