"""This module is for lottery simulation and analytic tool."""

from __future__ import absolute_import
from __future__ import print_function

from mode import *

def main(start=1, end=50, length=4):
	print('Welcome to the lottery simulation system.')
	while True:
		game(start, end, length)
		again = input("Again? (Y/N): ")
		if again != 'Y':
			break

def game(*args):
	mode = select_mode()
	exec_mode(mode, *args)

def select_mode():
	print("Mode 1 : Create a new simulation.")
	print("Mode 2 : Load previous simulation.")
	mode_code = input("Please select the mode (type 1 or 2) : ")
	return mode_code

def exec_mode(mode_code, *args):
	name = 'mode_%s'%mode_code
	mode = globals().get(name)

	if mode is not None:
		mode(*args)
	else:
		raise NotImplementedError("Mode_%s not implemented."%mode_code)

if __name__ == "__main__":
	main()
