import hashlib


class Salesperson:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = self.hash_password(password)
    
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

    @property   
    def password(self):
        return self.password_hash 
    
    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'password_hash': self.password_hash
        }

    def __str__(self):
        return f"Salesperson(name={self.name}, email={self.email})"