import pygal


from die import Die


# cria um d6
die_1 = Die()
die_2 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)
	
	
# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)


# Visualiza  os resultados
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['2', '3' , '4' , '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Reseult"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
