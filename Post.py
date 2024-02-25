from abc import ABC, abstractmethod
from PIL import Image
from matplotlib import pyplot as plt
from enum import Enum


# Implemented using Factory Design Pattern. A user in
# the Social Network creates different types of 'Post'.
class PostType(str, Enum):
    TEXT = "Text"
    IMAGE = "Image"
    SALE = "Sale"


class Post(ABC):
    def __init__(self, post_type):
        self.post_type = post_type
        self.comments = []
        self.likes = []
        self._author = None

    def like(self, user):
        self.likes.append(user)
        if user is not self._author:
            print(f"notification to {self._author.username}: {user.username} liked your post")
            self._author.notify(f"{user.username} liked your post")

    def comment(self, user, text):
        self.comments.append('username:' + user.username + ' text:' + text)
        if user != self._author:
            print(f"notification to {self._author.username}: {user.username} commented on your post: {text}")
            self._author.notify(f"{user.username} commented on your post")

    @abstractmethod
    def display(self):
        pass

    def __str__(self):
        if self.post_type == "Image":
            return f"{self._author.username} posted a picture\n"
        else:
            return f"{self.display() or ''}"


class TextPost(Post):
    def __init__(self, content):
        super().__init__(PostType.TEXT)
        self.content = content

    def display(self):
        print(f"{self._author.username} published a post:\n\"{self.content}\"")


class ImagePost(Post):
    def __init__(self, image_path):
        super().__init__(PostType.IMAGE)
        self.image_path = image_path

    def display(self):
        print("Shows picture")
        try:
            # Using Matplotlib to display the image
            img_matplotlib = plt.imread(self.image_path)
            plt.imshow(img_matplotlib)
            plt.axis('off')  # Turn off axis labels
            plt.show()

            # Using Pillow to display the image (optional)
            img_pillow = Image.open(self.image_path)
            img_pillow.show()

            return "Displayed an image."
        except Exception as e:
            return f"Error displaying image: {str(e)}"


class SalePost(Post):
    def __init__(self, product, price, location):
        super().__init__(PostType.SALE)
        self.product = product
        self.price = price
        self.location = location
        self.is_sold = False

    def discount(self, discount, password):
        if self._author.password == password:
            self.price -= self.price / 100 * discount
            print(f"Discount on {self._author.username} product! the new price is: {self.price}")
        else:
            print("Wrong password")

    def sold(self, password):
        if self._author.password == password:
            self.is_sold = True
            print(f"{self._author.username}'s product is sold")

    def display(self):
        if not self.is_sold:
            print(
                f"{self._author.username} posted a product for sale:\nFor sale! {self.product}, price: {self.price}, pickup from: {self.location}")
            print()
        else:
            print(f"{self._author.username} posted a product for sale:")
            print(f"Sold! {self.product}, price: {self.price}, pickup from: {self.location}")


class PostFactory:
    @staticmethod
    def create_post(post_type, content=None, image_path=None, product=None, price=None, location=None):
        if post_type == PostType.TEXT:
            return TextPost(content)
        elif post_type == PostType.IMAGE:
            return ImagePost(image_path)
        elif post_type == PostType.SALE:
            return SalePost(product, price, location)
        else:
            raise ValueError(f"Invalid post type: {post_type}")
