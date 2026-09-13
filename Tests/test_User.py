import unittest
import hashlib

from Models.User import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(
            username="testuser",
            password="password123",
            email="john@example.com"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "john@example.com")
        self.assertEqual(self.user.role, "user")

    def test_password_is_hashed(self):
        expected_hash = hashlib.sha256(
            "password123".encode()
        ).hexdigest()

        self.assertEqual(
            self.user.password_hash,
            expected_hash
        )

    def test_hash_password(self):
        password = "test123"
        expected_hash = hashlib.sha256(
            password.encode()
        ).hexdigest()

        self.assertEqual(
            self.user._hash_password(password),
            expected_hash
        )

    def test_to_dict(self):
        user_dict = self.user.to_dict()

        self.assertEqual(user_dict["username"], "testuser")
        self.assertEqual(user_dict["email"], "john@example.com")
        self.assertEqual(user_dict["role"], "user")
        self.assertEqual(
            user_dict["password_hash"],
            self.user.password_hash
        )

    def test_str_representation(self):
        self.assertEqual(
            str(self.user),
            "testuser"
        )


if __name__ == "__main__":
    unittest.main()