from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
def index_employee(employee_id, employee_data):
    es.index(index="employee_index", id=employee_id,document=employee_data)
    print(f"Employee {employee_id} indexed successfully!")
    
def search_employees_by_department(department):
    query = {
        "query": {
            "term": {
                "department.keyword": department
           }
       }
    }
    result = es.search(index="employee_index", body=query)
    return result['hits']['hits']
def get_employee(employee_id):
      result = es.get(index="employee_index", id=employee_id)
      return result['_source']
if __name__ == "__main__":
  employeeid = input("enter the employee id: ")
  employeename = input("Enter the employee name: ")
  employeetile = input("Enter the job title: ")
  employeedepartment = input('Enter the employee department: ')
  bussinessunit = input('Enter the employee bussinessunit: ')
  gender = input('Enter the employee gender: ')
  ethnicity = input('Enter the employee ethnicity: ')
  age = input('Enter the employee age: ')
  hire_date = input('Enter the employee hire_date: ')
  annual_salary = input('Enter the employee annual_salary: ')
  bonus_percentage = input('Enter the employee bonus_percentage: ')
  country = input('Enter the employee country: ')
  city = input('Enter the employee city: ')
  employee_data = {
      "employee_id": int(employeeid),
      "full_name": employeename,
      "job_title":employeetile,
      "department": employeedepartment,
      "business_unit": bussinessunit,
      "gender": gender,
      "ethnicity": ethnicity,
      "age": int(age),
      "hire_date": hire_date,
      "annual_salary": float(annual_salary),
      "bonus_percentage": float(bonus_percentage),
      "country": country,
      "city":city,
      "exit_date": None
}
index_employee(1, employee_data)
employees = search_employees_by_department("Engineering")
print("Employees in Engineering department:", employees)
employee = get_employee(1)
print("Employee Details:", employee)