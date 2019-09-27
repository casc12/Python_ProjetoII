import requests


# Faz a chamda a API e armazena a resposta
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)


#Armazena a resposta da API em uma variável 
response_dict = r.json()
#processa o resultado
print("Total repositories:", response_dict['total_count'])

#Explora Informações sobre os repositórios
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))


# Analisa o Primeiro repositório
#repo_dict = repo_dicts[0]


print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
	print('\nName: ', repo_dict['name'])
	print('Owner: ', repo_dict['owner']['login'])
	print('Stars: ',repo_dict['stargazers_count'])
	print('Repository: ',repo_dict['html_url'])
	print('Created: ', repo_dict['created_at'])
	print('Update: ',repo_dict['updated_at'])
	print('Discription: ', repo_dict['description'])
"""print("\nKeys:", len(repo_dict))

for key in sorted(repo_dict.keys()):
	print(key)"""
