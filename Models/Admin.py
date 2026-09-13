from Models.User import User

class Admin(User):
    def __init__(self, username, password, email):
        
        super().__init__(username, password, role="admin")
        self.email = email  

    
    def to_dict(self):
        data = super().to_dict()
        data["email"] = self.email
        return data