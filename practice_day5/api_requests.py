import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
user_data = response.json()
print(f"Tên người dùng từ API: {user_data['name']}")
print(f"Email: {user_data['email']}")