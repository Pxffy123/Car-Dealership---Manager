import unittest
import hashlib

from Models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(
            username="testuser",
            password="password123",
            email="john@example.com"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "john")
        self.assertEqual(self.user.email, "john@examole.com")
        self.assertEqual(self.user.role, "user")
    
    def test_password_hashing(self):
        expected_hash = hashlib.sha256("password123".encode()).hexdigest()

        self.assertEqual(self.user.password_hash, expected_hash)