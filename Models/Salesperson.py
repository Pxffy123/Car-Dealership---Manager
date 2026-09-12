import hashlib


class Salesperson:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = self.hash_password(password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()