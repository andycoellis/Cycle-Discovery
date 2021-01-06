def solution(n, b):
	# Code to be written
	return 'Not implemented'


class IdNumber:
	""" 
	The IdNumbers class creates an object that represents a number to a
	given base input. Arguments given are:

	n:-	(string) number in desired base format, i.e. base=3 given number would be 231
	b:- (int) base number of desired IdNumber

	Example IdNumber(n='231578', b=10) woud create a standard base 10 number.

	"""
	def __init__(self, n, b):
		if not isinstance(n, str) or not isinstance(b, int):
			raise TypeError('Input n must be either a string or integer')

		for i in range(0, len(n)):
			if b < 1 or b > 10:
				raise ValueError('Only numbers between and including base 1 and 10')
			if not int(n[i]) < b:
				raise ValueError('Given string is not in base power supplied')

		self.base = b

		self.number = n
		self.base10 = self.convert_to_base10()

		self.length = len(self.number)



	def __sub__(self, o):
		""" This will return a string of the operators result """
		if not isinstance(o, IdNumber):
			raise TypeError('This operator only works between two IdNumber objects')
		if self.base != o.base:
			raise TypeError('Two IdNumbers do not have equivalent base numbers')
		if self.length != o.length:
			raise TypeError('Two IdNumbers must have the same length')

		res = self.base10 - o.base10

		if res < 0:
			raise ValueError('This class can not compute negative numbers')

		return self.convert_base10_to_baseN(res)



	def __add__(self, o):
		""" This will return a string of the operators result """
		if not isinstance(o, IdNumber):
			raise TypeError('This operator only works between two IdNumber objects')
		if self.base != o.base:
			raise TypeError('Two IdNumbers do not have equivalent base numbers')
		if self.length != o.length:
			raise TypeError('Two IdNumbers must have the same length')

		res = self.base10 + o.base10

		return self.convert_base10_to_baseN(res)



	def convert_to_base10(self):
		p = 1	# Identifies which position we are evaluating
		d = 0	# Initial decimal number

		# Loop will travel in reverse
		for i in range(len(self.number)-1, -1, -1):
			d += int(self.number[i]) * p
			# Adjust power for next index evaluation
			p = p * self.base

		return d


	def convert_base10_to_baseN(self, base10):
		""" Will convert a decimal number into n base number """
		k = base10

		response = ""
		while k > 0:
			response = response + str(k % self.base)
			k = k // self.base

		return self.reformat_string_length(response[::-1])


	def reformat_string_length(self, n):
		""" Returns a string that prepends 0 if necessary to sustain original string length """
		res = ['0'] * self.length

		for i in range(0, len(n)):
			res[i + (self.length - len(n))] = n[i]

		return "".join(res)

