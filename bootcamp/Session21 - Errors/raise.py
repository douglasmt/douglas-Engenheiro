def colorize(text, color):
	colors = ("cyan", "yellow", "blue", "green", "magenta")
	if type(text) is not str:
		raise TypeError("text must be instance of str")
	if type(color) is not str:
		raise TypeError("Color must be string")
	if color not in colors:
		raise ValueError("color is invalid color")
	print(f"Printed {text} in {color}")

#colorize([], 'cyan')
#colorize(34, "red")
#colorize("Color selected", "red")
#colorize("Color selected", "green")
colorize("Color selected", {"green"})
