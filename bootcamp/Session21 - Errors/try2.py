# try:
# except:
# else:
# finally:


while True:
	try:
		num = int(input("please enter a number: "))
	except ValueError: 	#if there is an invalid character
		print("That's not a number!")
	else: 				# if there is a valid character
		print("Good job, you entered a number!")
		break
	finally: 			# runs anyway
		print("RUNS NO MATTER WHAT!")
print("REST OF GAME LOGIC RUNS!")

# try:
# 	num = int(input("please enter a number: "))
# except:
# 	print("That's not a number!")
# else:
# 	print("I'M IN THE ELSE!")
# finally:
# 	print("RUNS NO MATTER WHAT!")

