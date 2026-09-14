import hashlib


class User:
    
    def __init__(self, username, password, email=None, role="user"):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.email = email
        self.role = role

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()   

    def to_dict(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "email": self.email,
            "role": self.role
        }

    def __str__(self):
        return self.username
