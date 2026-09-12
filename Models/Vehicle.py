class Vehicle:
    def_init_(self,vehicle_id,make,model,year,price,mileage,
            color,status="Available"):

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

            def_str_(self):
                return(
                    f"{self.vehicle_id}:"
                    f"{self.year}{self.make}{self.model}"
                    f"-KSH{self.price:,.2f}"
                )    

