import requests

API_KEY = "186fdb3d7c8c4ef7fc9d7481d6d9315c"
API_SECRET = "22e45a7ba2d0bab0b8ce03addeceb419"

response = requests.get("https://api.mailjet.com/v3/rest/contact",
                        auth=(API_KEY, API_SECRET))

print(f"Status Code: {response.status_code}")
print(response.text)
