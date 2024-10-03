from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
def search_employee_by_id(employee_id):
    try:
        result = es.get(index="employee_index", id=employee_id)
        employee_data = result['_source']
        return employee_data
    except Exception as e:
         print(f"Error: {e}")
         return None
if __name__ == "__main__":
   employee_id = input('Enter the employee ID: ')
employee = search_employee_by_id(employee_id)
if employee:
   print("Employee found:", employee)
else:
   print(f"Employee with ID {employee_id} not found.") 