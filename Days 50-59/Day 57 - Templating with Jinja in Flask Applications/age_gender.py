import requests


def get_age(name):

    params = {
        "name": name
    }

    response = requests.get("https://api.agify.io", params=params)
    response.raise_for_status()
    data = response.json()
    return data['age']


def get_gender(name):

    params = {
        "name": name
    }

    response = requests.get("https://api.genderize.io", params=params)
    response.raise_for_status()
    data = response.json()
    return data['gender']


print(get_gender("jesus"))
