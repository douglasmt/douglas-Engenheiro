from csv import DictReader, DictWriter

def cm_to_in(cm):
	return float(cm) * 0.393701

with open('../01_316/fighters.csv') as file:
	csv_reader = DictReader(file)	
	fighters = list(csv_reader)

with open("inches_fighters.csv", "w") as file:
	headers = ("Name","Country","Height")
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	for f in fighters:
		csv_writer.writerow({
			"Name": f["Name"],
			"Country": f["Country"],
			"Height": cm_to_in(f["Height (in cm)"]) # float(cm) * 0.393701
		})

# csv_writer.writeheader() 		 -> step 1
# csv_writer.writerow( dict..  ) -> step 2

