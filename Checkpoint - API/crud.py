import requests

url = 'http://localhost:5000/livros'

novo_livro = {
    "titulo": "Diario de um Banana",
    "autor": "Jeff Kinney",
    "preco": 29.90,
    "data_publicacao": "2007-04-01"
}

#Operação POST
response = requests.post(url, json=novo_livro)
print(response.json(),response.status_code)

#Operação GET
response = requests.get(f"url/{1}")
print(response.json(),response.status_code)

#Operação DELETE
response = requests.delete(f"url/{1}")
print(response.json(),response.status_code)

#Operação PUT
#Operação DELETE
response = requests.put(f"url/{1}")
print(response.json(),response.status_code)