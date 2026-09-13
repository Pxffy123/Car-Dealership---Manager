from Models.Salesperson import Salesperson
from Models.User import User


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
        "jane.doe@example.com",
        sales_target=10
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

    assert salesperson.password != "securepassword"
    assert len(salesperson.password) == 64


def test_salesperson_to_dict():
    salesperson = Salesperson(
        "john_doe",
        "password123",
        "john.doe@example.com",
        sales_target=10
    )

    data = salesperson.to_dict()

    assert data["username"] == "john_doe"
    assert data["email"] == "john.doe@example.com"
    assert data["role"] == "salesperson"
    assert data["sales_target"] == 10
    assert data["total_sales"] == 0
    assert "password_hash" in data


def test_salesperson_str_representation():
    salesperson = Salesperson(
        "jane_doe",
        "password123",
        "jane.doe@example.com",
        sales_target=10
    )

    assert str(salesperson) == (
        "Salesperson(username=jane_doe, email=jane.doe@example.com)"
    )