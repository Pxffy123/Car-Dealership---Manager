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