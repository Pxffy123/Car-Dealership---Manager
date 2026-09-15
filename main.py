from pathlib import Path

from Models.Vehicle import Vehicle
from Utils.auth import AuthManager
from Utils.storage import load_json, save_json


VEHICLES_FILE = Path("Data/Vehicles.json")


class CarDealershipApp:
    def __init__(self):
        self.auth_manager = AuthManager()
        self.current_user = None

    # ==================================================
    # APPLICATION
    # ==================================================

    def run(self):
        while True:
            if self.current_user is None:
                self.logged_out_menu()
            else:
                self.logged_in_menu()

    # ==================================================
    # LOGGED OUT MENU
    # ==================================================

    def logged_out_menu(self):
        print("\n" + "=" * 45)
        print("   CAR DEALERSHIP MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. Register")
        print("2. Login")
        print("3. View Vehicles")
        print("4. Search Vehicles")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            self.register()

        elif choice == "2":
            self.login()

        elif choice == "3":
            self.view_vehicles()

        elif choice == "4":
            self.search_vehicles()

        elif choice == "5":
            self.exit_application()

        else:
            print("Invalid choice. Please try again.")

    # ==================================================
    # LOGGED IN MENU
    # ==================================================

    def logged_in_menu(self):
        print("\n" + "=" * 45)
        print("   CAR DEALERSHIP MANAGEMENT SYSTEM")
        print("=" * 45)
        print(f"Logged in as: {self.current_user.username}")
        print(f"Role: {self.current_user.role}")
        print("-" * 45)

        print("1. View Vehicles")
        print("2. Search Vehicles")
        print("3. View Vehicle Details")
        print("4. Sell Vehicle")

        if self.current_user.role == "admin":
            print("5. Add Vehicle")
            print("6. Update Vehicle Status")
            print("7. Delete Vehicle")

        print("8. Logout")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()
        print(f"Debug: choice = {repr(choice)}")  # Debugging line

        if choice == "1":
            self.view_vehicles()

        elif choice == "2":
            self.search_vehicles()

        elif choice == "3":
            self.view_vehicle_details()

        elif choice == "4":
            self.sell_vehicle()

        elif choice == "5" and self.current_user.role == "admin":
            self.add_vehicle()

        elif choice == "6" and self.current_user.role == "admin":
            self.update_vehicle_status()

        elif choice == "7" and self.current_user.role == "admin":
            self.delete_vehicle()

        elif choice == "8":
            self.logout()

        elif choice == "9":
            self.exit_application()

        else:
            print("Invalid choice or insufficient permissions.")

    # ==================================================
    # AUTHENTICATION
    # ==================================================

    def register(self):
        print("\n--- REGISTER ---")

        username = input("Username: ").strip()
        password = input("Password: ").strip()
        email = input("Email (optional): ").strip()

        print("\nSelect account type:")
        print("1. User")
        print("2. Salesperson")
        print("3. Admin")

        role_choice = input("Enter choice: ").strip()

        roles = {
            "1": "user",
            "2": "salesperson",
            "3": "admin"
        }

        role = roles.get(role_choice)

        if role is None:
            print("Invalid account type.")
            return

        try:
            user = self.auth_manager.register(
                username=username,
                password=password,
                email=email,
                role=role
            )

            print("\nRegistration successful!")
            print(f"Welcome, {user.username}.")

        except ValueError as error:
            print(f"\nRegistration failed: {error}")

    def login(self):
        print("\n--- LOGIN ---")

        username = input("Username: ").strip()
        password = input("Password: ").strip()

        user = self.auth_manager.login(username, password)

        if user:
            self.current_user = user

            print("\nLogin successful!")
            print(f"Welcome, {user.username}!")
            print(f"Role: {user.role}")

        else:
            print("\nInvalid username or password.")

    def logout(self):
        if self.current_user:
            print(f"\nGoodbye, {self.current_user.username}!")

        self.current_user = None

    def exit_application(self):
        print("\nThank you for using the Car Dealership Management System.")
        raise SystemExit

    # ==================================================
    # VEHICLE HELPERS
    # ==================================================

    def load_vehicles(self):
        data = load_json(VEHICLES_FILE)

        vehicles = []

        for item in data:
            vehicle = Vehicle(
                vehicle_id=item["vehicle_id"],
                make=item["make"],
                model=item["model"],
                year=item["year"],
                price=item["price"],
                mileage=item["mileage"],
                color=item["color"],
                status=item.get("status", "Available")
            )

            vehicles.append(vehicle)

        return vehicles

    def save_vehicles(self, vehicles):
        data = []

        for vehicle in vehicles:
            data.append({
                "vehicle_id": vehicle.vehicle_id,
                "make": vehicle.make,
                "model": vehicle.model,
                "year": vehicle.year,
                "price": vehicle.price,
                "mileage": vehicle.mileage,
                "color": vehicle.color,
                "status": vehicle.status
            })

        save_json(VEHICLES_FILE, data)

    # ==================================================
    # VIEW VEHICLES
    # ==================================================

    def view_vehicles(self):
        print("\n--- VEHICLES ---")

        vehicles = self.load_vehicles()

        if not vehicles:
            print("No vehicles found.")
            return

        for vehicle in vehicles:
            print(vehicle)
            print(f"   Mileage: {vehicle.mileage}")
            print(f"   Color: {vehicle.color}")
            print(f"   Status: {vehicle.status}")
            print("-" * 45)

    # ==================================================
    # SEARCH VEHICLES
    # ==================================================

    def search_vehicles(self):
        print("\n--- SEARCH VEHICLES ---")

        search_text = input(
            "Enter vehicle ID, make, or model: "
        ).strip().lower()

        if not search_text:
            print("Search cannot be empty.")
            return

        vehicles = self.load_vehicles()

        results = [
            vehicle
            for vehicle in vehicles
            if search_text in vehicle.vehicle_id.lower()
            or search_text in vehicle.make.lower()
            or search_text in vehicle.model.lower()
        ]

        if not results:
            print("No matching vehicles found.")
            return

        print(f"\nFound {len(results)} vehicle(s):")

        for vehicle in results:
            print(vehicle)
            print(f"   Mileage: {vehicle.mileage}")
            print(f"   Color: {vehicle.color}")
            print(f"   Status: {vehicle.status}")
            print("-" * 45)

    # ==================================================
    # VEHICLE DETAILS
    # ==================================================

    def view_vehicle_details(self):
        print("\n--- VEHICLE DETAILS ---")

        vehicle_id = input("Enter vehicle ID: ").strip()

        vehicles = self.load_vehicles()

        for vehicle in vehicles:
            if vehicle.vehicle_id.lower() == vehicle_id.lower():
                print(f"\nVehicle ID: {vehicle.vehicle_id}")
                print(f"Make: {vehicle.make}")
                print(f"Model: {vehicle.model}")
                print(f"Year: {vehicle.year}")
                print(f"Price: KSh {vehicle.price:,.2f}")
                print(f"Mileage: {vehicle.mileage}")
                print(f"Color: {vehicle.color}")
                print(f"Status: {vehicle.status}")
                return

        print("Vehicle not found.")

    # ==================================================
    # ADD VEHICLE
    # ==================================================

    def add_vehicle(self):
        if self.current_user.role != "admin":
            print("Admin access required.")
            return

        print("\n--- ADD VEHICLE ---")

        vehicle_id = input("Vehicle ID: ").strip()
        make = input("Make: ").strip()
        model = input("Model: ").strip()
        color = input("Color: ").strip()

        try:
            year = int(input("Year: ").strip())
            price = float(input("Price: ").strip())
            mileage = int(input("Mileage: ").strip())
        except ValueError:
            print("Year, price, and mileage must be valid numbers.")
            return

        vehicles = self.load_vehicles()

        for vehicle in vehicles:
            if vehicle.vehicle_id.lower() == vehicle_id.lower():
                print("A vehicle with that ID already exists.")
                return

        vehicle = Vehicle(
            vehicle_id=vehicle_id,
            make=make,
            model=model,
            year=year,
            price=price,
            mileage=mileage,
            color=color
        )

        vehicles.append(vehicle)
        self.save_vehicles(vehicles)

        print("\nVehicle added successfully!")
        print(vehicle)

    # ==================================================
    # SELL VEHICLE
    # ==================================================

    def sell_vehicle(self):
        print("\n--- SELL VEHICLE ---")

        vehicle_id = input("Enter vehicle ID: ").strip()

        vehicles = self.load_vehicles()

        for vehicle in vehicles:
            if vehicle.vehicle_id.lower() == vehicle_id.lower():

                if vehicle.sell():
                    self.save_vehicles(vehicles)
                    print("\nVehicle sold successfully!")
                    print(vehicle)
                else:
                    print("This vehicle has already been sold.")

                return

        print("Vehicle not found.")

    # ==================================================
    # UPDATE STATUS
    # ==================================================

    def update_vehicle_status(self):
        if self.current_user.role != "admin":
            print("Admin access required.")
            return

        print("\n--- UPDATE VEHICLE STATUS ---")

        vehicle_id = input("Enter vehicle ID: ").strip()

        new_status = input(
            "Enter new status (Available/Sold): "
        ).strip().title()

        if new_status not in ("Available", "Sold"):
            print("Invalid status.")
            return

        vehicles = self.load_vehicles()

        for vehicle in vehicles:
            if vehicle.vehicle_id.lower() == vehicle_id.lower():
                vehicle.status = new_status
                self.save_vehicles(vehicles)

                print("Vehicle status updated successfully.")
                return

        print("Vehicle not found.")

    # ==================================================
    # DELETE VEHICLE
    # ==================================================

    def delete_vehicle(self):
        if self.current_user.role != "admin":
            print("Admin access required.")
            return

        print("\n--- DELETE VEHICLE ---")

        vehicle_id = input("Enter vehicle ID: ").strip()

        vehicles = self.load_vehicles()

        for vehicle in vehicles:
            if vehicle.vehicle_id.lower() == vehicle_id.lower():

                confirmation = input(
                    "Are you sure you want to delete this vehicle? (yes/no): "
                ).strip().lower()

                if confirmation != "yes":
                    print("Deletion cancelled.")
                    return

                vehicles.remove(vehicle)
                self.save_vehicles(vehicles)

                print("Vehicle deleted successfully.")
                return

        print("Vehicle not found.")


if __name__ == "__main__":
    app = CarDealershipApp()
    app.run()