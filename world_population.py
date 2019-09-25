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
		else:
			print('ERROR - '+ country_name)

#Agrupa países em três níveis populacionais
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_poplations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
		
	elif pop < 1000000000:
		cc_pops_2[cc]=pop
		
	else:
		cc_pops_3[cc]= pop
# Vê quantos países estão em cada nível 
print(len(cc_pops_1), len(cc_pops_1), len(cc_pops_3))

wm = World()
wm.title='World Population in 2010, by Country'
#wm.add('2010', cc_poplations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)


wm.render_to_file('world_population.svg')
