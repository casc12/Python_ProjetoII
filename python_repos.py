import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

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
"""print("Repositories returned:", len(repo_dicts))


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
print("\nKeys:", len(repo_dict))

for key in sorted(repo_dict.keys()):
	print(key)"""
print("Number of items: ", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	#stars.append(repo_dict['stargazers_count'])
	description = repo_dict['description']
	if not description:
		description = "No description provided."
	plot_dict = {
	'value': repo_dict['stargazers_count'],
	'label': description,
	'xlink': repo_dict['html_url'],
	}
	plot_dicts.append(plot_dict)
# Cria a Visualização
my_style = LS('#333366', base_style=LCS)


my_config = pygal.Config()
my_config.x_label_rotation =45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart= pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
print(plot_dict)
chart.render_to_file('python_repos.svg')
