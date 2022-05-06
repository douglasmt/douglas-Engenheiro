from csv import DictReader, DictWriter

def cm_to_in(cm):
	return float(cm) * 0.393701

with open('../01_316/fighters.csv') as file:
	csv_reader = DictReader(file)	
	fighters = list(csv_reader)

with open("inches_fighters_header.csv", "w") as file:
	headers = ("Name","Country","Height")
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()