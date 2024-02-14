class Employee:
    def __init__(self, name, id, title, department) -> None:
        self.name = name
        self.id = id
        self.title = title
        self.department = department

    def employee_details(self, ):
        employee_details = {
           "name":self.name,
           "id":self.id, 
           "title":self.title, 
           "department":self.department, 
        }
        print(employee_details)

    def __str__(self) -> str:
        return "employee name: {name} and ID: {id}".format(self.name, self.id)
    
class Department(Employee):
    def __init__(self, department_name, list_of_employee) -> None:
        self.department_name = department_name
        self.list_of_employee = []

    def add_employee(self, employee):
        self.list_of_employee.append(employee)
    def remove_employee(self, employee_id):
        for emp in self.list_of_employee:
            if emp.employee_id == employee_id:
                self.list_of_employee.remove(emp)
                print(f"Employee {emp.name} removed from the department {self.name}")
                return
        print(f"Employee is not foundwith id {employee_id} in this department {self.name}")

    def list_employees(self):
        print(f"Employees in department {self.name}:")
        for emp in self.employees:
            print(emp)
     

# Main code #
try:
    emp1 = Employee("sharukhan", 357, "Software Engineer", "Electronics")
    emp2 = Employee("rampradhosh", 102, "Tester", "ComputerScience")
    engineering_dept = Department("Electronics")
    data_science_dept = Department("ComputerScience")
    # Adding employees to departments
    engineering_dept.add_employee(emp1)
    data_science_dept.add_employee(emp2)
    # Displaying employees in departments
    engineering_dept.list_employees()
    data_science_dept.list_employees()
    # Removing employee from department
    engineering_dept.remove_employee(1001)
        
    # Displaying updated list of employees in department
    engineering_dept.list_employees()
except Exception as e:
    print(str(e))