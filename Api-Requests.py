import requests
req=requests.get(url="http://127.0.0.1:9000/api/")
print(req.json())