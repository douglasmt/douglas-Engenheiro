

from csv import DictReader
def print_users():

    with open("users.csv") as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            # Each row is an OrderedDict!
            print(row['First Name'] + ' ' + row['Last Name'] ) #Use keys to access data

print_users() # None

'''
import csv
 
def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader: 
            print("{} {}".format(row['First Name'], row['Last Name']))
'''