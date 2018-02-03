from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import with_statement

from tempfile import gettempdir as _gettempdir
import os as _os

import numpy as _np

from util import get_all_states as _get_all_states
from util import get_states_number as _get_states_number
from util import is_jackpot as _is_jackpot
from util import select_prize_nums as _select_prize

__all__ = ['mode_1', 'mode_2', 'mode_3']

_TMP_DIR = _gettempdir()
_DIR = _os.path.join(_TMP_DIR, 'lottory')

def mode_1(*args):
	"""Create a new lottery simulation and save result under system temporary directory
	"""
	print("================= Create mode =================")

	prize_nums = _select_prize()

	filename = input('Please input filename: ')
	filepath = _os.path.join(_DIR, filename)

	if not _os.path.exists(_DIR):
		_os.mkdir(_DIR)

	print("Simulating......")
	all_states = _get_all_states(*args)
	states_num = _get_states_number(*args)
	data = _np.zeros(states_num)

	for key, pair in zip(range(states_num), all_states):
		data[key] = _is_jackpot(pair, prize_nums)
	
	_np.save(filepath, data)

	filepath += '.npy'
	filesize = _os.stat(filepath).st_size
	print("Simulation is over")
	print("File save at %s. Total filesize %s bytes"%(filepath, filesize))


def mode_2(*args):
	"""Load data from the previous simulation"""
	# TODO
	print("================= Load mode =================")

	filename = input("PLease input filename: ")
	filepath = _os.path.join(_DIR, filename)
	filepath += '.npy'
	filesize = _os.stat(filepath).st_size

	try:
		print("Loading file......")
		data = _np.load(filepath)
		print("FInish loading. Total file size %s bytes"%filesize)
	except FileNotFoundError as ex:
		print("File not found. Please try again")
		return 

	all_states = _get_all_states(*args)

def mode_3(*args):
	#TODO
	pass
