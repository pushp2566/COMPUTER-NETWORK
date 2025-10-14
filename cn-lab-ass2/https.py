import requests

# GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    print("Status:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)
else:
    print("GET request failed")

# POST request
data = {"title": "Hello", "body": "This is a test", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
if response.status_code == 201:
    print("Status:", response.status_code)
    print("Response:", response.json())
else:
    print("POST request failed")
