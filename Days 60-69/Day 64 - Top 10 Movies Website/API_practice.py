import requests as req
import os
from dotenv import load_dotenv

load_dotenv()

apik = os.getenv("api_key")
token = os.getenv("bearer_token")

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {token}"
}

params = {
    "query": "Gladiator"
}

res = req.get(url="https://api.themoviedb.org/3/search/movie", headers=headers, params=params)
res.raise_for_status()
data = res.json()
print(data)