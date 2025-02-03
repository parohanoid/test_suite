import requests

url = "https://dummyjson.com/auth/login"

payload = {
  "username": "emilys",
  "password": "emilyspass"
}
headers = {
  "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())