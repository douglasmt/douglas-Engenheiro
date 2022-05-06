from csv import reader, writer
# Other approach, with only 1 file open at a time
with open('../01_316/fighters.csv') as file:
	csv_reader = reader(file)
	
	# data converted to list and saved to variable
	# (differece from 02_scream.py: using fighters in the next with open)
	fighters = [[s.upper() for s in row] for row in csv_reader]
	
	# the file to be read at the writer has the headers
	# NAME|COUNTRY|HEIGHT (IN CM)
	# RYU|JAPAN|175

with open('screaming_fighters_03.csv', "w") as file:
	csv_writer = writer(file)
	for fighter in fighters:
		# the file to be read at the writer has the headers (fighters variable above)
		# NAME|COUNTRY|HEIGHT (IN CM)
	 	# RYU|JAPAN|175
		csv_writer.writerow(fighter)
