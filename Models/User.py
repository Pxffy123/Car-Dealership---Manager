import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()   

    def login(self):
        pass

    def __str__(self):
        return self.username
