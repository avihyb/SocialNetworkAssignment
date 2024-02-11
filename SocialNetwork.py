from User import User


class SocialNetwork:
    _created = False

    def __init__(self, name):
        if SocialNetwork._created:
            raise RuntimeError("SocialNetwork already created")
        self.users = []
        self.name = name
        SocialNetwork._created = True
        print("The social network {name} was created!")

    def sign_up(self, username, password):
        if any(user.username == username for user in self.users):
            print(f"Username '{username}' is already taken. Please choose a different username.")
            return
        try:
            new_user = User(username, password)
            self.users.append(new_user)
        except ValueError as e:
            print(e)
