import requests

endpoint = "http://localhost:8000/product/6/update"

data = {
    "title": "Hello Darkness my old friend",
    "price": 129.99
}

get_response = requests.put(endpoint, json=data)

print(get_response.text)
print(get_response.status_code)
# print(get_response.json())
