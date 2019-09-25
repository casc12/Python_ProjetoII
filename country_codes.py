from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
	"""Devolve o código de duas letras do Pygal para um país, dado o seu nome."""
	for code, name  in COUNTRIES.items():
		if name == country_name:
			return code
		# Se o país  não for encontrado, devolve None
	return None
		
"""print(get_country_code('Brazil'))
print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))"""
