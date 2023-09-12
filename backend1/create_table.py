import requests

response = requests.post('http://localhost:5000/create_tables')
print(response.json())