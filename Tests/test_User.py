import unittest
import sys
from pathlib import Path


root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

# Now these imports will work flawlessly!
from Models.User import User
from Models.Admin import Admin
from Models.Salesperson import Salesperson

class TestUserModels(unittest.TestCase):

    def test_user_password_hashing(self):
        """Verify that User models cleanly hash raw passwords on creation."""
        customer = User("kamau_buyer", "my_secret_pass")
        self.assertEqual(customer.username, "kamau_buyer")
        self.assertEqual(customer.role, "user")
        self.assertNotEqual(customer.password_hash, "my_secret_pass")

    def test_admin_inheritance(self):
        """Verify Admin properly inherits and configures permissions."""
        boss = Admin("super_admin", "boss123", "boss@dealership.co.ke")
        self.assertEqual(boss.role, "admin")
        self.assertEqual(boss.email, "boss@dealership.co.ke")

    def test_salesperson_inheritance(self):
        """Verify Salesperson inherits from User and tracks sales data."""
        seller = Salesperson("juma_sales", "sellcars123")
        self.assertEqual(seller.role, "salesperson")
        self.assertEqual(seller.total_sales, 0)

if __name__ == "__main__":
    unittest.main()
