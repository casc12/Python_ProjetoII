import requests


# Faz a chamda a API e armazena a resposta
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)


#Armazena a resposta da API em uma variável 
response_dict = r.json()
#processa o resultado
print(response_dict.keys())
