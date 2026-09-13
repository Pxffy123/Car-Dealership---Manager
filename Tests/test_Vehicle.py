import unittest

from Models.Vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(
            vehicle_id="V001",
            make="Toyota",
            model="Camry",
            year=2020,
            price=25000,
            mileage=15000,
            color="Red"
        )

    def test_vehicle_creation(self):
        self.assertEqual(self.vehicle.vehicle_id, "V001")
        self.assertEqual(self.vehicle.make, "Toyota")
        self.assertEqual(self.vehicle.model, "Camry")
        self.assertEqual(self.vehicle.year, 2020)
        self.assertEqual(self.vehicle.price, 25000)
        self.assertEqual(self.vehicle.mileage, 15000)
        self.assertEqual(self.vehicle.color, "Red")
        self.assertEqual(self.vehicle.status, "Available")

    def test_default_status(self):
        self.assertEqual(self.vehicle.status, "Available")
        
    def test_sell_vehicle(self):
        result = self.vehicle.sell()
        self.assertTrue(result)
        self.assertEqual(self.vehicle.status, "Sold")

    def test_sell_already_sold_vehicle(self):
        self.vehicle.sell()  # Sell the vehicle first
        result = self.vehicle.sell()  # Try to sell again
        self.assertFalse(result)
        self.assertEqual(self.vehicle.status, "Sold")

    def test_str_representation(self):
        expected_str = "V001: 2020 Toyota Camry - KSH 25,000.00"
        self.assertEqual(str(self.vehicle), expected_str)

if __name__ == "__main__":
    unittest.main()