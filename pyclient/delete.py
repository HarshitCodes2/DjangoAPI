import requests

endpoint = "http://localhost:8000/product/6/delete"

get_response = requests.delete(endpoint)

print(get_response.text)
print(get_response.status_code)
# print(get_response.json())
