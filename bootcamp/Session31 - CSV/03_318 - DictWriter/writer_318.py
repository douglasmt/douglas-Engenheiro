from csv import writer, DictWriter
# Version using writer
# with open("cats.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Name", "Age"])
#     csv_writer.writerow(["Blue", 3])
#     csv_writer.writerow(["Kitty", 1])

# Version using DictWriter
with open("cats.csv", "w") as file: 
	# overwrite the file if it has any data
	# with open("cats.csv", "a") as file: writes new lines and leaves the old one
	headers = ["Name", "Breed", "Age"]
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader() 	# only writes the header
	csv_writer.writerow({ 		# only writes the first line
		"Name": "Garfield",
		"Breed": "Orange Tabby",
		"Age": 10
	})
