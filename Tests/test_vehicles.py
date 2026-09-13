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