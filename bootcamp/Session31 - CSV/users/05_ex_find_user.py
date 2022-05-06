import csv
def find_user(first,last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (row, value) in enumerate(csv_reader):
            #if first == row['First Name'] and last == row['Last Name']:
            #if first == value[0] and last == value[1]:
            first_name_match = first == value[0]
            last_name_match = last == value[1]
            if first_name_match and last_name_match:
                return row
            #else:
            #    return first + ' ' + last + ' not found.'
        return "{} {} not found.".format(first, last)


'''
def find_user(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return "{} {} not found.".format(first_name, last_name)'''
print(find_user("Colt", "Steele")) # 1
print(find_user("Alan", "Turing")) # 3
print(find_user("Not", "Here")) 

'''
import csv
 
def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader: 
            print("{} {}".format(row['First Name'], row['Last Name']))
'''