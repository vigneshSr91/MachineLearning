import sys
variables = ['In', 'Out', 'exit', 'quit', 'get_iptyhon', 'variables']

# Get a sorted list of objects and their sizes
sorted([(x, sys.getsizeof(globals().get(x))) for x in dir() 
		if not x.startswith('_') and x not in sys.modules and 
		x not in variables], key=lambda x: x[1], reverse=True)
