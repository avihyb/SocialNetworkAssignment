from User import User


class SocialNetwork:
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
        result = f"{self.name} social network:"
        display_content = self.display()
        if display_content:
            result += f"\n{display_content}"
        return result

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
            user.disconnect()
            print(f"{username} disconnected")
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
        user_list = [str(user) for user in self.users]
        return '\n'.join(user_list).rstrip('\n')

    def print(self):
        for user in self.users:
            print(f"User name: {user}, Number of posts: {user.posts.size}, Number of followers: {user.followers.size}")
