from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
def update_employee_by_id(employee_id, updated_data):
    try:
       result = es.update(
            index="employee_index",
            id=employee_id,
            body={
               "doc": updated_data
            }
       )
       print(f"Employee with ID {employee_id} updated successfully.")
       return result
    except Exception as e:
      print(f"Error updating employee with ID {employee_id}: {e}")
      return None
if __name__ == "__main__":
     employee_id = 1
     updated_data = {
         "job_title": "Senior Software Engineer",
         "annual_salary": 95000,
         "bonus_percentage": 12.0
}
update_employee_by_id(employee_id, updated_data)