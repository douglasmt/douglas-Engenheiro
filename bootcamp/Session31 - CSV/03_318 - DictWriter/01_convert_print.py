from csv import DictReader, DictWriter

def cm_to_in(cm):
	return float(cm) * 0.393701

with open('../01_316/fighters.csv') as file:
	csv_reader = DictReader(file)
	print(list(csv_reader))