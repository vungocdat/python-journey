import pyfiglet
from termcolor import colored

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

msg = input("What would you like to print? ")
color = input("What color? ")

# set default color if invalid color name is provided
if color not in valid_colors:
    color = "magenta"

ascii_msg = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_msg, color=color)
print(colored_ascii)
