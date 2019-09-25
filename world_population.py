import json

from pygal.maps.world import World
from country_codes import get_country_code


#Carrega os dados em uma lista

filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
	

# Exibe a população de cada país em 2010
# Constrói um dicionário com dados das populações
cc_poplations = {}
for pop_dict in pop_data:
	
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		#print(country_name+": "+str(population))
		if code:
			#print(code+": "+str(population))
			cc_poplations[code] = population
		"""else:
			print('ERROR - '+ country_name)"""

wm = World()
wm.title='World Population in 2010, by Country'
wm.add('2010', cc_poplations)


wm.render_to_file('world_population.svg')
