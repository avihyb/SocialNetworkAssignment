from User import User


class SocialNetwork:
    # flag used to tell
    # whether a social network has already been created:
    _created = False

    def __init__(self, name):
        # Singleton Design Pattern: creating only one object of SocialNetwork
        if SocialNetwork._created:
            raise RuntimeError("SocialNetwork already created")
        self.users = []
        self.posts = []
        self.name = name
        SocialNetwork._created = True
        print(f"The social network {name} was created!")

    def __str__(self):
        print(f"{self.name} social network:")
        return f"{self.display() or ''}"

    def sign_up(self, username, password):
        if any(user.username == username for user in self.users):
            print(f"Username '{username}' is already taken. Please choose a different username.")
            return None

        try:
            new_user = User(username, password)
            self.users.append(new_user)
            return new_user
        except ValueError as e:
            print(e)

    def log_out(self, username):
        user = next((user for user in self.users if user.username == username), None)
        if user:
            if user.status:
                user.disconnect()
                print(f"{username} disconnected")
            else:
                print(f"{username} is already logged out.")
        else:
            print(f"{username} not found in the social network.")

    def log_in(self, username, password):
        user = next((user for user in self.users if user.username == username and user.password == password), None)
        if user:
            user.connect()
            print(f"{username} connected")
        else:
            print(f"{username} not found in the social network.")

    def add_post(self, post):
        self.posts.append(post)

    def display(self):
        for user in self.users:
            print(user)

    def print(self):
        for user in self.users:
            print(f"User name: {user}, Number of posts: {user.posts.size}, Number of followers: {user.followers.size}")
