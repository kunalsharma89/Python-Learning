# Employee Management System

A simple command-line Employee Management System in Python that allows you to add, view, and search for employees. Employee data is stored in a dictionary for easy access and management.

## Features
- Add new employees with unique Employee IDs
- View all employees in a table-like format
- Search for employees by Employee ID
- Input validation for Employee ID and other details
- User-friendly menu system

## Usage
1. Run the program:
   ```
   python EMS.py
   ```
2. Follow the on-screen menu to:
   - Add Employee
   - View All Employees
   - Search for Employee
   - Exit

## Project Structure
- `EMS.py`: Main program file containing all logic and functions

## How It Works
- Employee data is stored in a dictionary, with Employee ID as the key and details as a nested dictionary.
- The program uses functions for each operation to keep the code organized.
- The menu system loops until the user chooses to exit.

## Example Employee Data
```
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Amit', 'age': 32, 'department': 'Finance', 'salary': 60000},
    103: {'name': 'Priya', 'age': 29, 'department': 'IT', 'salary': 65000},
    104: {'name': 'John', 'age': 35, 'department': 'Marketing', 'salary': 55000}
}
```

## Requirements
- Python 3.x

## License
This project is for educational purposes.
