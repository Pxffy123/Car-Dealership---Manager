import hashlib

class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        
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



class Admin(User):
    def __init__(self, username, password, email):
        
        super().__init__(username, password, role="admin")
        self.email = email  

    
    def to_dict(self):
        data = super().to_dict()
        data["email"] = self.email
        return data
