from csv import DictReader, DictWriter

def add_user(first, last):
    with open("users.csv", "a") as file:
        headers = ("First Name","Last Name")
        csv_writer = DictWriter(file, fieldnames=headers)
        #csv_writer.writeheader()
        csv_writer.writerow({
            
            "First Name": first,
            "Last Name": last
            
        })

add_user("Dwayne", "Johnson") # None
add_user("Colt", "Steele") # None

