import requests


response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
response.raise_for_status()
allPosts = response.json()


class Post:
    def __init__(self, title, subtitle, description):
        self.title = title
        self.subtitle = subtitle
        self.description = description


def get_posts_list():
    posts_list = []

    for post in allPosts:
        new_post = Post(post["title"], post["subtitle"], post["body"])
        posts_list.append(new_post)

    return posts_list
