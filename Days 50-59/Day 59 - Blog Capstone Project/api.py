import requests

res = requests.get("https://api.npoint.io/002e90ad79f718da35e7")
res.raise_for_status()
res = res.json()

print(res[0]["title"])
