class User:
    def __init__(self, username):
        self.username = username
        self.auth = False


def auth_decorator(function):
    def wrapper(*args, **kwargs):
        if (args[0].auth == True):
            function(args[0])
    return wrapper


@auth_decorator
def make_post(user):
    print(f"This is {user.username}'s post. Hello :3")


anto = User("Anto")
anto.auth = True
make_post(anto)
