import argparse

class arguments():
	def __init__(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('-t', action='store_true', dest = 'test',
							default = False,
							help='Turn on testing mode',
							)
		parser.add_argument('-s', action='store_true', dest = 'socket',
							default = False,
							help='Turn on LED socket',
							)
		parser.add_argument('-b', action='store_true', dest = 'bluetooth',
							default = False,
							help='Turn on bluetooth listener',
							)
		parser.add_argument('-x', action='store_true', dest = 'xbox',
							default = False,
							help='Turn on xbox listener',
							)
		self.results = parser.parse_args()
