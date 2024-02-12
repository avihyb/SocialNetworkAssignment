from Post import TextPost, ImagePost, SalePost


class User:

    def __init__(self, username, password):
        if not (4 <= len(password) <= 8):
            raise ValueError("Password must be between 4 and 8 characters.")
        self.username = username
        self.password = password
        self.status = True
        self.followers = []
        self.following = []
        self.posts = []
        self.notifications = []

    def __str__(self):
        return f"User name: {self.username}, Number of posts: {len(self.posts)}, Number of followers: {len(self.followers) or ' '}"

    def disconnect(self):
        self.status = False

    def connect(self):
        self.status = True

    def notifications_manager(self):
        pass

    def notify(self, message):
        self.notifications.append(message)

    def follow(self, user):
        if user not in self.following:
            self.following.append(user)
            user.followers.append(self)
            print(f"{self.username} started following {user.username}")

    def unfollow(self, user):
        if user in self.following:
            self.following.remove(user)
            user.followers.remove(self)
            print(f"{self.username} unfollowed {user.username}")

    def publish_post(self, post_type, *args):
        post = None
        if not self.status:
            print("User is not connected. Cannot publish post.")
            return None

        if post_type == "Text":
            post = TextPost(*args)
        elif post_type == "Image":
            print(f"{self.username} posted a picture")
            print()
            post = ImagePost(*args)
        elif post_type == "Sale":
            post = SalePost(*args)
        if post:
            post._author = self
            self.posts.append(post)
            for follower in self.followers:
                follower.notify(f"{self.username} has a new post")
            if post_type != "Image":
                post.display()
                if post.post_type == "Text":
                    print()
            return post
        else:
            print(f"Invalid post type: {post_type}")
            return None

    def print_notifications(self):
        if self.status:
            print(f"{self.username}'s notifications:")
            for notification in self.notifications:
                if notification is not None:
                    print(f"{notification}")

