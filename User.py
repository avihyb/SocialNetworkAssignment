class User:
    def __init__(self, username, password):
        if not (4 <= len(password) <= 8):
            raise ValueError("Password must be between 4 and 8 characters.")
        self.username = username
        self.password = password


    def
