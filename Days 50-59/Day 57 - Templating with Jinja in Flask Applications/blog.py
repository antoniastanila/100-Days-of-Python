import requests


def get_all_posts():
    res = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = res.json()
    return all_posts
