class Employee:
    def __init__(self, emp_id, name, age, department):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department

    def __str__(self):
        return f'ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Department: {self.department}'

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, age, department):
        new_employee = Employee(emp_id, name, age, department)
        self.employees.append(new_employee)
        print(f'Employee {name} added successfully.')

    def view_employees(self):
        if not self.employees:
            print('No employees found.')
        else:
            for emp in self.employees:
                print(emp)

    def remove_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print(f'Employee ID {emp_id} removed successfully.')
                return
        print(f'Employee ID {emp_id} not found.')

def main():
    manager = EmployeeManager()
    
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Remove Employee")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            department = input("Enter Department: ")
            manager.add_employee(emp_id, name, age, department)
        elif choice == '2':
            manager.view_employees()
        elif choice == '3':
            emp_id = input("Enter Employee ID to remove: ")
            manager.remove_employee(emp_id)
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
