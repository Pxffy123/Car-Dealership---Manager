from pathlib import Path
from Models.User import User
from Models.Admin import Admin
from Models.Salesperson import Salesperson
from Utils.storage import load_json, save_json
from Utils.validators import not_empty, valid_email

class AuthManager:
    def __init__(self, users_file="Data/Users.json"):
        self.users_file = Path(users_file)

    def register(self, username, password, email=None, role="user"):
        username = username.strip()
        role = role.strip().lower()
        if email:
            email = email.strip().lower()

        if not not_empty(username):
            raise ValueError("Username cannot be empty.")
        if email and not valid_email(email):
            raise ValueError("Please enter a valid email.")
        if len(password) < 4:
            raise ValueError("Password must have at least 4 characters.")
        if role not in ("user", "admin", "salesperson"):
            raise ValueError("Role must be user, admin, or salesperson.")

        users = load_json(self.users_file)

        for saved_user in users:
            if saved_user["username"].lower() == username.lower():
                raise ValueError("An account with that username already exists.")

        # Create the correct object (they hash passwords automatically upon creation now)
        if role == "admin":
            if not email:
                raise ValueError("Admin accounts require an email.")
            user = Admin(username, password, email)
        elif role == "salesperson":
            user = Salesperson(username, password, email=email)
        else:
            user = User(username, password, email=email, role=role)

        users.append(user.to_dict())
        save_json(self.users_file, users)
        return user

    def login(self, username, password):
        username = username.strip()
        users = load_json(self.users_file)
        
        # We instantiate a temporary user to cleanly get the hash of the entered password
        temp = User(username, password)

        for saved_user in users:
            if saved_user["username"].lower() == username.lower():
                if saved_user["password_hash"] == temp.password_hash:
                    # Rebuild the correct object matching our models
                    if saved_user["role"] == "admin":
                        return Admin(saved_user["username"], password, saved_user.get("email"))
                    elif saved_user["role"] == "salesperson":
                        return Salesperson(saved_user["username"], password, saved_user.get("email"), saved_user.get("sales_target", 0))
                    else:
                        return User(saved_user["username"], password, saved_user.get("email"), saved_user["role"])
        return None