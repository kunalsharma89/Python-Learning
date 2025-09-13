# Employee data dictionary
employees = {
	101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
	102: {'name': 'Amit', 'age': 32, 'department': 'Finance', 'salary': 60000},
	103: {'name': 'Priya', 'age': 29, 'department': 'IT', 'salary': 65000},
	104: {'name': 'John', 'age': 35, 'department': 'Marketing', 'salary': 55000}
}


def main_menu():
	while True:
		print("\nEmployee Management System")
		print("1. Add Employee")
		print("2. View All Employees")
		print("3. Search for Employee")
		print("4. Exit")
		choice = input("Enter your choice (1-4): ")
		if choice == '1':
			add_employee()
		elif choice == '2':
			view_employees()
		elif choice == '3':
			search_employee()
		elif choice == '4':
			print("Thank you for using the Employee Management System. Goodbye!")
			break
		else:
			print("Invalid choice. Please enter a number between 1 and 4.")

def add_employee():
	while True:
		try:
			emp_id = int(input("Enter Employee ID: "))
			if emp_id in employees:
				print("Employee ID already exists. Please enter a new ID.")
			else:
				break
		except ValueError:
			print("Invalid input. Please enter a valid integer for Employee ID.")
	try:
		name = input("Enter Employee Name: ")
		age = int(input("Enter Employee Age: "))
		department = input("Enter Employee Department: ")
		salary = float(input("Enter Employee Salary: "))
		employees[emp_id] = {
			'name': name,
			'age': age,
			'department': department,
			'salary': salary
		}
		print("Employee added successfully.")
	except ValueError:
		print("Invalid input. Please enter correct data types.")

def view_employees():
	if not employees:
		print("No employees available.")
	else:
		print("\n{:<10} {:<20} {:<5} {:<15} {:<10}".format('Emp ID', 'Name', 'Age', 'Department', 'Salary'))
		print("-"*60)
		for emp_id, details in employees.items():
			print("{:<10} {:<20} {:<5} {:<15} {:<10}".format(
				emp_id,
				details['name'],
				details['age'],
				details['department'],
				details['salary']
			))

def search_employee():
	try:
		search_id = int(input("Enter Employee ID to search: "))
		if search_id in employees:
			details = employees[search_id]
			print(f"\nEmployee Details for ID {search_id}:")
			print(f"Name: {details['name']}")
			print(f"Age: {details['age']}")
			print(f"Department: {details['department']}")
			print(f"Salary: {details['salary']}")
		else:
			print("Employee not found.")
	except ValueError:
		print("Invalid input. Please enter a valid integer for Employee ID.")

if __name__ == "__main__":
	main_menu()
