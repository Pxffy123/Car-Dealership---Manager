from pathlib import Path

from Utils.storage import load_json, save_json


class Vehicle:
    
    def __init__(self, vehicle_id, make, model, year, price, mileage, color, status="Available"):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.price = price  
        self.mileage = mileage
        self.color = color
        self.status = status

    def sell(self):
        if self.status == "Sold":
            return False
        self.status = "Sold"
        return True



    
    def to_dict(self):
        return {
            "vehicle_id": self.vehicle_id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "price": self.price,
            "mileage": self.mileage,
            "color": self.color,
            "status": self.status
        }

    
    def __str__(self):
        return (
            f"{self.vehicle_id}: "
            f"{self.year} {self.make} {self.model} "
            f"- KSh {self.price:,.2f}"
        )


class CarCollection:

    def __init__(self, cars_file="Data/Vehicles.json"):
        self.cars_file = Path(cars_file)

    def _load_cars(self):
        return [Vehicle.from_dict(item) for item in load_json(self.cars_file)]

    def _save_cars(self, cars):
        save_json(self.cars_file, [cars.to_dict() for car in cars])

    def add_car(self, car):
        books = self._load_cars()
        books.append(car)
        self._save_cars(car)

    def view_car(self):
        return self._load_cars()

    def search_car(self, search_text):
        search_text = search_text.lower()
        return [
            car
            for car in self._load_cars()
            if search_text in car.title.lower()
            or search_text in car.author.lower()
        ]

    def update_status(self, title, new_status):
        cars = self._load_cars()

        for car in cars:
            if car.title.lower() == title.lower():
                car.status = new_status
                self._save_cars(cars)
                return True

        return False

    def delete_car(self, title):
        cars = self._load_cars()

        for car in cars:
            if car.title.lower() == title.lower():
                cars.remove(car)
                self._save_cars(cars)
                return True

        return False