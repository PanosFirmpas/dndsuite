import random
import datetime
import time


def get_roll(die,how_many):
	die,how_many = int(die),int(how_many)
	results = []
	for d in range(how_many):
		result = random.randint(1,die)
		results.append(result)
	return results

def roll():
	message = '[{3}] {2}>> Rolled {1} d{0} dice and got: '
	r_number = 0
	while 1:
		arguments = raw_input('roll(die,how_many): ')
		if arguments.endswith(' '):
			arguments = arguments[:-1]

		arguments = arguments.split(' ')
		arguments = [int(x) for x in arguments]
		
		
		
		if len(arguments) == 1:
			arguments.append(1)

		

		results = get_roll(*arguments)

		ts = time.time()
		dt = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
		
		
		al = arguments+[dt,r_number]


		print message.format(*al), results
		r_number += 1
