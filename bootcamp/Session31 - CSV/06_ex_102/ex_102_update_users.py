'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''
from csv import reader, writer

def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = reader(csvfile)
        rows = list(csv_reader)

    count_updated = 0

    with open("users.csv", "w") as csvfile:
        # file users.csv has it's data erased to reinsert from 'rows' object
        csv_writer = writer(csvfile)
        for user in rows: 
            
            if user[0] == old_first and user[1] == old_last:

                csv_writer.writerow([new_first,new_last]) 
                # updates the line from the 'rows' object
                count_updated += 1
                print("User: {}, {} and try {} {}".format(user[0], user[1], old_first, old_last))
                print(count_updated)
            else:
                csv_writer.writerow(user)
                # write the rows again from the 'rows' object with all lines

    return "Users updated: {}.".format(count_updated)

print(update_users("Grace", "Hopper", "Hello", "World")) # Users updated: 1.
print(update_users("Colt", "Steele", "Boba", "Fett")) # Users updated: 2.
print(update_users("Not", "Here", "Still not", "Here")) # Users updated: 0.