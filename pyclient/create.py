import requests

endpoint = "http://localhost:8000/product/create"


get_response = requests.post(endpoint, data={"title": "test4", "price": 120.00})

print(get_response.text)
print(get_response.status_code)
# print(get_response.json())
