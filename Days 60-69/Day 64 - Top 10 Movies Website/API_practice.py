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
results = res.json()['results']

movies_and_dates = []
for result in results:
    movies_and_dates.append((result['title'], result['release_date']))

for elements in movies_and_dates:
    print(f"{elements[0]} - {elements[1]}\n")


url = "https://api.themoviedb.org/3/movie/98?language=en-US"

response = req.get(url, headers=headers)
print(response.json()["poster_path"])