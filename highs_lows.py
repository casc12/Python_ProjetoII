import csv

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	#print(header_row)
	highs = []
	for row in reader:
		high = int(row[1])
		highs.append(high)
		
		
		
	print(highs)
	
