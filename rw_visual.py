import matplotlib.pyplot as plt

from random_walk import RandomWalk


# continua Criando novos passeios aleatórios 
while True:
	# Cria um passeio aleatório
	rw = RandomWalk(50000)
	rw.fill_walk()
	
	
	# Define o tamanho da Janela de plotagem
	plt.figure(dpi=128, figsize=(10,6))
	
	
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
	
	#Enfatiza o primeiro e o último ponto
	plt.scatter(0, 0, c='orange', edgecolor='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='silver', edgecolor='none', s=100)
	
	
	# Remove os eixos
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()
	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break 
