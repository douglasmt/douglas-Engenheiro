from termcolor import colored

text = colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)
text = colored("HI THERE!", color="magenta")
print(text)
text = colored("HI THERE!", color="yellow", on_color="on_magenta")
print(text)
