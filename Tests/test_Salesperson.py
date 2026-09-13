from models.Salesperson import Salesperson
from models.User import User

def test_salesperson_is_a_user():
    salesperson = Salesperson(
        "john_doe", 
        "password123", 
        "john.doe@example.com"
    )
    assert isinstance(salesperson, User)

def test_salesperson_details():
    salesperson = Salesperson(
        "jane_doe", 
        "password123", 
        
        "jane.doe@example.com"
    )
    assert salesperson.username == "jane_doe"
    assert salesperson.email == "jane.doe@example.com"
    assert salesperson.role == "salesperson"
    assert salesperson.sales_target == 10
    assert salesperson.total_sales == 0

def test_salesperson_password_is_hashed():
    salesperson = Salesperson(
        "alice_smith", 
        "securepassword", 
        "alice.smith@example.com"
    )
    assert salesperson.password != "securepassword"  # Ensure the password is hashed
    assert len(salesperson.password) == 64  # Ensure the hashed password is not empty

def test_salesperson_to_dict():
    salesperson = Salesperson(
        "john_doe", 
        "password123",
        "john.doe@example.com"
        sales_target=10
    )