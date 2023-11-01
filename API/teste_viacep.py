import requests

dado = requests.get("https://viacep.com.br/ws/01538-001/json")

if dado.ok():
    info = dado.json()
    print(info)
else:
    print("erro na consulta")
