import requests
import json

# URL for Elasticsearch endpoint
url = "http://localhost:9200/employee_index"

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

# Body of the request with settings and mappings
body = {
    "settings": {
        "number_of_shards": 3,
        "number_of_replicas": 1
    },
    "mappings": {
        "properties": {
            "employee_id": {"type": "integer"},
            "full_name": {"type": "text"},
            "job_title": {"type": "text"},
            "department": {"type": "keyword"},
            "business_unit": {"type": "keyword"},
            "gender": {"type": "keyword"},
            "ethnicity": {"type": "keyword"},
            "age": {"type": "integer"},
            "hire_date": {"type": "date", "format": "yyyy-MM-dd"},
            "annual_salary": {"type": "float"},
            "bonus_percentage": {"type": "float"},
            "country": {"type": "keyword"},
            "city": {"type": "keyword"},
            "exit_date": {"type": "date", "format": "yyyy-MM-dd", "null_value": None}
        }
    }
}

# Sending the PUT request to create the index
response = requests.put(url, headers=headers, data=json.dumps(body))

# Printing the response from the server
print(response.status_code)
print(response.json())

