import requests

url = "http://localhost:8000/invoke"

response = requests.post(url, json={
    "input": "Hello introduce yourself"
})

print(f"Response status code: {response.status_code}")

if response.status_code == 200:
    print(response.json())