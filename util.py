from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from itertools import combinations as _cb
from itertools import product as _product
from math import factorial as _factorial

import re as _re

__all__ = ['get_all_states', 'is_jackpot', 'select_prize_nums']

def is_jackpot(odds_evens_tup, prize_nums):
	odds, evens= odds_evens_tup
	if set(odds) & prize_nums and set(evens) & prize_nums:
		return True
	else:
		return False

def select_prize_nums():
	raw_inputs = input("Select prize numbers: ")

	regex = '\d+'
	processed_inputs = _re.findall(regex, raw_inputs)
	prize_nums = set(map(int, processed_inputs))

	return prize_nums

def get_states_number(start, end , length):
	curr_l = (start-end)//2 + 1
	curr_s = (start+end+1)//2
	nom = 1
	for _ in range(length):
		nom *= curr_l * curr_s
		curr_l -= 1
		curr_s -= 1
	denom = _factorial(length)
	denom *= denom
	result = nom//denom

	return result

def get_all_states(start, end, length):
	odds_gen = _get_odds_cb_gen(start, end, length)
	evens_gen = _get_evens_cb_gen(start, end, length)

	return _product(odds_gen, evens_gen)

def _get_odds_cb_gen(start, end, length):
	"""return the generator of all combinations of the given 
	length from all odd numbers x , where start <= x <= end 
	* input type:
		start 	: int
		end 	: int
		length	: int
	* return type : ((int,)) 
	"""
	first_odd = start if start % 2 == 1 else start + 1
	odds_gen = range(first_odd, end + 1, 2)
	odds_cb_gen = _cb(odds_gen, length)

	return odds_cb_gen

def _get_evens_cb_gen(start, end, length):
	"""return the generator of all combinations of the given 
	length from all even numbers x , where start <= x <= end 
	* input type:
		start 	: int
		end 	: int
		length	: int
	* return type : ((int,))
	"""
	first_even = start if start % 2 == 0 else start + 1
	evens_gen = range(first_even, end + 1, 2)
	evens_cb_gen = _cb(evens_gen, length)

	return evens_cb_gen
