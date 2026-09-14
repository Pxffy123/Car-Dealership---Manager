import sys
from pathlib import Path


root_path = Path(__file__).resolve().parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

from Models.Vehicle import Vehicle, CarCollection
from Utils.auth import AuthManager
from Utils.Decorators import login_required, admin_required
from Utils.storage import load_json, save_json

class DealershipApp:
    def __init__(self):
        self.auth = AuthManager()
        self.collection = CarCollection()
        self.current_user = None  

    def seed_default_admin(self):
        
        users = load_json(self.auth.users_file)
        if not users:
            print("[!] Seeding default system account...")
            self.auth.register("admin", "admin123", "admin@dealership.co.ke", "admin")

    def public_registration(self):
         #public acc's can register too ....................................
        print("\n--- 👤 REGISTER ACCOUNT ---")
        username = input("Enter Username: ").strip()
        password = input("Enter Password (min 4 chars): ").strip()
        email = input("Enter Email Address (NOT❌ optional(dont guess😡)): ").strip()
        if not email:
            email = None

        try:
            
            new_user = self.auth.register(username, password, email, role="user")
            print(f"🎉 Account successfully created for '{new_user.username}'! You can now log in.")
        except ValueError as e:
            print(f"❌ Registration Failed: {e}")

    @login_required
    def view_inventory(self):
        cars = self.collection.view_cars()
        if not cars:
            print("🚘 The showroom is currently empty mate(add cars if u an admin)😭.")
        for car in cars:
            print(car)

    @login_required
    def search_inventory(self):
        query = input("Search by ID, Make, or Model: ").strip()
        results = self.collection.search_car(query)
        if not results:
            print("🔍 No vehicles matched your search.")
        for car in results:
            print(car)

    @admin_required
    def add_vehicle(self):
        print("\n--- 📝 ADD NEW VEHICLE ---")
        v_id = input("Enter Vehicle ID (e.g., CAR001): ").strip()
        make = input("Enter Make (e.g., Lamborghini🏎️): ").strip()
        model = input("Enter Model (e.g., Gallardo): ").strip()
        year = input("Enter Year: ").strip()
        price = input("Enter Price (KSh): ").strip()
        mileage = input("Enter Mileage (km): ").strip()
        color = input("Enter Color: ").strip()
        
        new_car = Vehicle(v_id, make, model, year, price, mileage, color)
        self.collection.add_car(new_car)
        print(f"✅ Vehicle {v_id} successfully added to database.")

    @admin_required
    def remove_vehicle(self):
        v_id = input("Enter Vehicle ID to delete: ").strip()
        if self.collection.delete_car(v_id):
            print(f"🗑️ Vehicle {v_id} deleted successfully.")
        else:
            print("❌ Vehicle ID not found.")

    @login_required
    def sell_vehicle(self):
        if self.current_user.role != "salesperson" and self.current_user.role != "admin":
            print("❌ Access Denied: Only Salespersons or Admins can issue sales transactions.")
            return
        
        v_id = input("Enter Vehicle ID to sell: ").strip()
        cars = self.collection.view_cars()
        target_car = next((c for c in cars if c.vehicle_id.lower() == v_id.lower()), None)
        
        if target_car:
            if target_car.sell():
                self.collection.update_status(v_id, "Sold")
                print(f"🎉 Success! KSh {target_car.price:,.2f} transaction logged. Car marked as SOLD.")
            else:
                print("⚠️ This vehicle has already been sold.")
        else:
            print("❌ Vehicle ID not found.")

    def run(self):
        self.seed_default_admin()
        while True:
            if not self.current_user:
                print("\n=== 🏎️ CAR DEALERSHIP SYSTEM ===")
                print("1. Login")
                print("2. Register Account")
                print("3. Leave!!!")
                choice = input("Select choice (1-3): ").strip()
                
                if choice == "1":
                    username = input("Username: ").strip()
                    password = input("Password: ").strip()
                    user = self.auth.login(username, password)
                    if user:
                        self.current_user = user
                        print(f"\n👋 Access Granted. Welcome back, {user.username} [{user.role.upper()}]... the GOAT🐐")
                    else:
                        print("❌ Invalid credentials.")
                elif choice == "2":
                    self.public_registration()
                elif choice == "3":
                    print("Exiting. Goodbye!")
                    sys.exit()
            else:
                
                print(f"\n--- MAIN MENU ({self.current_user.role.upper()} PANEL) ---")
                
                if self.current_user.role == "admin":
                    print("1. View Full Vehicle Inventory")
                    print("2. Search for a Car")
                    print("3. Add New Vehicle")
                    print("4. Delete Vehicle")
                    print("5. Log Vehicle Sale Transaction")
                    print("6. Logout")
                    
                    choice = input("Select choice (1-6): ").strip()
                    if choice == "1": self.view_inventory()
                    elif choice == "2": self.search_inventory()
                    elif choice == "3": self.add_vehicle()
                    elif choice == "4": self.remove_vehicle()
                    elif choice == "5": self.sell_vehicle()
                    elif choice == "6": self.current_user = None
                    
                elif self.current_user.role == "salesperson":
                    print("1. View Full Vehicle Inventory")
                    print("2. Search for a Car")
                    print("3. Log Vehicle Sale Transaction")
                    print("4. Logout")
                    
                    choice = input("Select choice (1-4): ").strip()
                    if choice == "1": self.view_inventory()
                    elif choice == "2": self.search_inventory()
                    elif choice == "3": self.sell_vehicle()
                    elif choice == "4": self.current_user = None
                    
                else: 
                    print("1. View Available Showroom Cars")
                    print("2. Search for a Car")
                    print("3. Logout")
                    
                    choice = input("Select choice (1-3): ").strip()
                    if choice == "1": self.view_inventory()
                    elif choice == "2": self.search_inventory()
                    elif choice == "3": self.current_user = None

if __name__ == "__main__":
    app = DealershipApp()
    app.run()
