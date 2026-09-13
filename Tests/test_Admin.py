import unittest
from Models.Admin import Admin

class TestAdmin(unittest.TestCase):
    
    def setUp(self):
        self.admin = Admin(
            username="admin",
            password="admin123",
            email="admin@example.com"
        )
    
    def test_admin_creation(self):
        self.assertEqual(self.admin.username, "admin")
        self.assertEqual(self.admin.email, "admin@example.com")

    def test_admin_role(self):
        self.assertEqual(self.admin.role, "admin")