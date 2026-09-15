from Models.User import User


class Admin(User):
    def __init__(self, username, password, email):
       
        super().__init__(username, password, email=email, role="admin")

    def to_dict(self):
        
        return super().to_dict()   