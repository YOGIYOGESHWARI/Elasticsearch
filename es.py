from elasticsearch import Elasticsearch, helpers
import warnings


warnings.filterwarnings('ignore')
es = Elasticsearch("http://localhost:9200")


def createCollection(p_collection_name):
    if not es.indices.exists(index=p_collection_name.lower()):
        es.indices.create(index=p_collection_name.lower())
    print(f"Collection '{p_collection_name}' created successfully.")


def indexData(p_collection_name, employee_data):
    employee_id = employee_data['employee_id']
    es.index(index=p_collection_name.lower(), id=employee_id, document=employee_data)
    print(f"Employee {employee_id} indexed successfully!")


def searchByColumn(p_collection_name, p_column_name, p_column_value):
    query = {
        "query": {
            "term": {f"{p_column_name}.keyword": p_column_value}
        }
    }
    result = es.search(index=p_collection_name.lower(), body=query)
    return result['hits']['hits']


def getEmpCount(p_collection_name):
    if es.indices.exists(index=p_collection_name.lower()):
        count = es.count(index=p_collection_name.lower())['count']
        print(f"Employee count in '{p_collection_name}': {count}")
        return count
    print(f"Index '{p_collection_name}' does not exist.")
    return 0


def delEmpById(p_collection_name, p_employee_id):
    if es.exists(index=p_collection_name.lower(), id=p_employee_id):
        es.delete(index=p_collection_name.lower(), id=p_employee_id)
        print(f"Employee with ID '{p_employee_id}' deleted from '{p_collection_name}'.")
    else:
        print(f"Employee with ID '{p_employee_id}' not found in '{p_collection_name}'.")


def getDepFacet(p_collection_name):
    query = {
"size": 0,
        "aggs": {
            "departments": {
                "terms": {
                    "field": "department.keyword"
                }
            }
        }
    }
    result = es.search(index=p_collection_name.lower(), body=query)
    for bucket in result['aggregations']['departments']['buckets']:
        print(f"Department: {bucket['key']}, Count: {bucket['doc_count']}")
    return result['aggregations']['departments']['buckets']


employee_data = [
    {
        "employee_id": "E02001",
        "full_name": "Swetha",
        "job_title": "Software Engineer",
        "department": "IT",
        "gender": "Female",
        "age": 28,
        "hire_date": "2019-03-01",
        "annual_salary": 85000
    },
    {
        "employee_id": "E02003",
        "full_name": "Rithick",
        "job_title": "Project Manager",
        "department": "IT",
        "gender": "Male",
        "age": 35,
        "hire_date": "2017-04-15",
        "annual_salary": 95000
    }
]


if __name__ == "__main__":
    v_nameCollection = 'Hash_Yogeshwari'
    v_phoneCollection = 'Hash_9942299951'
    createCollection(v_nameCollection)
    createCollection(v_phoneCollection)


    getEmpCount(v_nameCollection)


    for employee in employee_data:
        indexData(v_nameCollection, employee)


    getEmpCount(v_nameCollection)


    delEmpById(v_nameCollection, 'E02003')


    getEmpCount(v_nameCollection)


    print(searchByColumn(v_nameCollection, 'department', 'IT'))
    print(searchByColumn(v_nameCollection, 'gender', 'Male'))
    print(searchByColumn(v_phoneCollection, 'department', 'IT'))


    getDepFacet(v_nameCollection)
    getDepFacet(v_phoneCollection)
