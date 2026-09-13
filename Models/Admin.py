import hashlib

class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        # Both classes now hash the plain password automatically on creation
        self.password_hash = self.hash_password(password)
        self.role = role

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password_hash == self.hash_password(password)

    def to_dict(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "role": self.role
        }

    def __str__(self):
        return self.username


# Admin inherits everything from User automatically
class Admin(User):
    def __init__(self, username, password, email):
        # Super sets up username, password hashing, and role="admin"
        super().__init__(username, password, role="admin")
        self.email = email  # Specific extra field for Admin

    # Overriding to_dict to include the email field
    def to_dict(self):
        data = super().to_dict()
        data["email"] = self.email
        return data
