import requests

token = None
headers =  {"Authorization" :f"Bearer {token}" 
,   "Dropbox-API-Arg" : "{\"path\" : \"/app-release.apk\"}" } 
url = "https://content.dropboxapi.com/2/files/download"


response = requests.get(url , headers=headers)

file = open("storage/shared/app.apk", "wb")
file.write(response.content)
file.close()
print("Done...")


"ALqLCKv6yf4AAAAAAAAAARNFAvzNzmiXL-2kK7Gpd5JBcCpXd1pNJhuIDg63x5x2"

