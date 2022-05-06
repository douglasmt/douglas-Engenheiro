'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''
from csv import reader, writer

def delete_users(del_first, del_last):
    with open("users.csv") as csvfile:
        csv_reader = reader(csvfile)
        rows = list(csv_reader)

    count_deleted = 0

    with open("users.csv", "w") as csvfile:
        csv_writer = writer(csvfile)
        for user in rows: 
            
            if user[0] == del_first and user[1] == del_last:
                count_deleted += 1
                print("User: {}, {} deleted".format(user[0], user[1]))
                print(count_deleted)
            else:
                csv_writer.writerow(user) 
                # write the rows again with the 'rows' object with all lines

    return "Users deleted: {}.".format(count_deleted)

print(delete_users("Grace", "Hopper")) # Users deleted: 1.
print(delete_users("Colt", "Steele")) # Users deleted: 2.
print(delete_users("Not", "Here")) # Users deleted: 0.