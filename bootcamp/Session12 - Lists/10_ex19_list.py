# Create a list called instructors
instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt","Blue", "Lisa"])
# Remove the last value in the list
instructors.remove("Lisa")
# Remove the first value in the list
instructors.remove("Colt")
# Add the string "Done" to the beginning of the list
instructors.insert(0,"Done")
# Run the tests to make sure you've done this correctly!
print(instructors)