from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
def delete_employee_by_id(employee_id):
     try:
        result = es.delete(index="employee_index", id=employee_id)
        print(f"Employee with ID {employee_id} deleted successfully.")
        return result
     except Exception as e:
        print(f"Error deleting employee with ID {employee_id}: {e}")
        return None
if __name__ == "__main__":
    employee_id = input('Enter the employee ID: ')
    delete_employee_by_id(employee_id)
                   