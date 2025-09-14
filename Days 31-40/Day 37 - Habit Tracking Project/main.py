import requests
import datetime

USERNAME = "your_username"
TOKEN = "your_token"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "graphy",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.now().strftime("%Y%m%d")
yesterday = datetime.datetime(2025, 9, 10).strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": input("How many minutes did u work today? ")
}

response = requests.post(
    url=post_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

new_pixel_data = {
    "quantity": "0"
}

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"


# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
