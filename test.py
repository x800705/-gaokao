import requests

a = requests.get("http://localhost:5000/blank")

print(a.text)
