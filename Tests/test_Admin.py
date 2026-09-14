import unittest
import shutil
from pathlib import Path
import sys

root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

from Utils.auth import AuthManager

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path("TestData_Auth")
        self.test_users_file = self.test_dir / "Users.json"
        self.auth = AuthManager(users_file=self.test_users_file)

    def tearDown(self):
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_auth_registration_and_login(self):
        """Verify AuthManager registers accounts and validates successful login cycles."""
        new_staff = self.auth.register("juma_sales", "sell123", role="salesperson")
        self.assertEqual(new_staff.role, "salesperson")
        
        logged_in_user = self.auth.login("juma_sales", "sell123")
        self.assertIsNotNone(logged_in_user)

    def test_auth_invalid_credentials(self):
        """Verify AuthManager blocks incorrect passwords."""
        self.auth.register("njeri_admin", "adminpass", "njeri@cars.com", "admin")
        bad_login = self.auth.login("njeri_admin", "wrong_pass")
        self.assertIsNone(bad_login)

if __name__ == "__main__":
    unittest.main()
