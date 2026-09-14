
===PROJECT===


# 🚘 Car Dealership Management System (GROUP 7🏎️🏎️)

A useful, OOP console application developed in Python to manage our car dealership inventory, staff roles, and client access securely. Our system here introduces advanced software engineering principles, including structural class inheritance, decoratorss, data validation, and JSON storage.

---

## ✨ Features & Architecture

The application defines a clear, hierarchical role-management permission framework that acts dynamically depending on the authenticated profile:

### 👥 User Roles & Access Matrix

| Feature | User(Public) | Salesperson | Admin |

| **Create Free Account** | ✅ | — | — | 
| **View Showroom Cars** | ❌ | ✅ | ✅ | ✅ 
| **Search Car Inventory** | ❌ | ✅ | ✅ | ✅
| **Log Vehicle Sale** | ❌ | ❌ | ✅ | ✅ 
| **Add/Delete Vehicles** | ❌ | ❌ | ❌ | ✅ 
| **Create Staff Accounts** | ❌ | ❌ | ❌ | ✅ 

### 🛠️ Core Infrastructure
* **Stateful Authorization:** Powered by native Python method wrapping (`@login_required`, `@admin_required`), that protects backend execution from unauthorized access blocks.
* **Persistent Engine:** Custom transactional state management utilities that automatically check file handles, process records gracefully, and serialize objects to clean JSON brackets (`Data/`).
* **Automated Data Seed:** The system features an intelligent cold-boot check. If `Users.json` is completely empty, it automatically injects fallback root credentials (`admin` / `admin123`) to ensure zero system dead-ends.

---

## 📂 Project Structure


Car_Dealership_Management_System/
│
├── Data/
│   ├── Users.json            
│   └── Vehicles.json          
├── Models/
│   ├── __init__.py
│   ├── User.py               
│   ├── Admin.py               
│   ├── Salesperson.py         
│   └── Vehicle.py            
├── Tests/
│   ├── __init__.py
│   └── test_dealership.py     
│
├── Utils/
│   ├── __init__.py
│   ├── auth.py               
│   ├── Decorators.py         
│   ├── storage.py           
│   └── validators.py          
│
└── main.py                   




 🚀 Execution & Setup

### Prerequisites
* Python 3.10 or higher.

### Step 1: Booting the Application
to excecute
-----------------------------------------
py main.py          #in terminal(Windows)

--------------------------------------------
*(On Windows systems, you can alternative use: `py main.py`)*

### Step 2:Login Credentials
If loading the database for the first time, log in using this administrator configuration:
* **Username:** `admin`
* **Password:** `admin123`

---

## Unit Testing

This repository is shipped with an automated testing ecosystem enforced by school grading requirements. The tests isolate live configurations into an automated sandbox file layout to protect production data during code assessment.

To execute the test suites directly from the root terminal path, run:
----------------------------------------------------------------------------
python -m unittest discover -s Tests
-----------------------------------------------------------------------------

The validation harness makes sure of:
1. **Password Hashing:** 
2. **Polymorphic Inheritance:** 
3. **Transactional Security:** 
4. **Auth State Flows:** 
