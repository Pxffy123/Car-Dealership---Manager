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

    def test_admin_password_hashing(self):
        self.assertNotEqual(self.admin.password_hash, "admin123")
        self.assertEqual(len(self.admin.password_hash), 64)

    def test_admin_to_dict(self):
        admin_data = self.admin.to_dict()
        self.assertEqual(admin_data["username"],  "admin")
        self.assertEqual(admin_data["email"], "admin@example.com")
        self.assertEqual(admin_data["role"], "admin")

    if __name__ == "__main__":
        unittest.main()