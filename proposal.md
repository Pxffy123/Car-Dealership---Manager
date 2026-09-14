# 🏎️ Group 7: Car Dealership Management System Proposal

### 1. Problem Definition
Small to mid-sized car dealerships often struggle to maintain accurate, up-to-date logs of available vehicle inventory, track distinct salesperson target achievements, and prevent transactional discrepancies (e.g., selling a car twice or unauthorized inventory manipulation). 

### 2. System Users & Features
* **Guest / Public User:** Can walk up to the console terminal, register an account for free, browse the active vehicle showroom, and search for specific cars.
* **Salesperson:** Can browse inventory and execute vehicle sales logs, which dynamically update a vehicle's status to 'Sold'.
* **Admin (Management):** Holds full authority to add new vehicles, remove vehicles from database persistence, register staff profiles, and seed the cold-boot system.

### 3. Planned Class Structures
* `User` (Base Model): Manages authentication vectors and handles native SHA-256 password hashing protocols.
* `Admin` (Extends User): Extends capabilities to allow administrative inventory and data adjustments.
* `Salesperson` (Extends User): Maps key transactional target metadata (e.g., `sales_target`, `total_sales`).
* `Vehicle`: Tracks structural car specifications (`vehicle_id`, `make`, `model`, `price`, `status`).
* `CarCollection`: Encapsulates database list manipulation, handling data mapping streams.

### 4. Database Storage & Authentication Strategy
Data is persistently stored across two structural JSON files (`Data/Users.json` and `Data/Vehicles.json`). Authentication is securely maintained using stateful validation decorators (`@login_required`, `@admin_required`) interacting with an `AuthManager` state framework, ensuring strict role-based access control.
