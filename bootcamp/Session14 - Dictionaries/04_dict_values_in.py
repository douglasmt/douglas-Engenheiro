# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!
# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = 0
for v in donations.values():
    total_donations += v


artist2 = {
    "first": "Paul",
    "last": "McCartney",
    "band": "Beatles",
}
if "Paul" in artist2.values():
    print(f"There is a Beatles musician! ")

if "band" in artist2.keys():
    print(f"There is a band in the data! ")

if "song" not in artist2.keys():
    print(f"There is no song in the data! ")


