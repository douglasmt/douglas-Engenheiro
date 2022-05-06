from csv import reader, writer
# using nested with statements
with open('../01_316/fighters.csv') as file:
	csv_reader = reader(file) #data never converted to list    
    #['Name', 'Country', 'Height (in cm)']
    #['Ryu', 'Japan', '175']

    # it has to be indented inside the 'with open' above
	with open('screaming_fighters_02.csv', "w") as file:
		csv_writer = writer(file)
		for fighter in csv_reader:
			csv_writer.writerow([s.upper() for s in fighter])