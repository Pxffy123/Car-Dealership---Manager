import unittest
import shutil
from pathlib import Path
import sys

root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

from Models.Vehicle import Vehicle, CarCollection

class TestVehicleCollection(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path("TestData_Vehicle")
        self.test_cars_file = self.test_dir / "Vehicles.json"
        self.collection = CarCollection(cars_file=self.test_cars_file)

    def tearDown(self):
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_vehicle_sales_flow(self):
        """Verify that cars are created as Available and flip safely to Sold."""
        car = Vehicle("V77", "Subaru", "Forester", 2018, 2500000, 45000, "Blue")
        self.assertEqual(car.status, "Available")
        
        self.assertTrue(car.sell())
        self.assertEqual(car.status, "Sold")

    def test_car_collection_persistence(self):
        """Verify CarCollection saves and pulls car data safely from JSON."""
        car = Vehicle("V99", "Mazda", "Demio", 2015, 950000, 80000, "Silver")
        self.collection.add_car(car)
        
        showroom = self.collection.view_cars()
        self.assertEqual(len(showroom), 1)
        self.assertEqual(showroom[0].make, "Mazda")

if __name__ == "__main__":
    unittest.main()
