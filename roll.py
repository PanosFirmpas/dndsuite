import random
import datetime
import time
import sys


def get_roll(how_many,die):
	die,how_many = int(die),int(how_many)
	results = []
	for d in range(how_many):
		result = random.randint(1,die)
		results.append(result)
	return results

def update(operator,num1,num2):
	if operator == '+':
		return num1 + num2
	elif operator == '-':
		return num1 - num2
	else:
		sys.exit('Unrecognized operator')


def roll():
	message = '[{2}] {1}>> Rolled {0} and got: '
	r_number = 0
	while 1:
		o_arguments = raw_input('roll(2d20+5): ')
		arguments = o_arguments

		for c in ['+','-',None]:
			l = arguments.split(c)
			if len(l) > 1:
				arguments,modifier = l
				break


		# if arguments.endswith(' '):
		# 	arguments = arguments[:-1]

		arguments = arguments.split('d')
		if len(arguments) != 2:
			print "Looks like you made a typo. Usage: '2d20', or '2d20+5', or '2d20-3', or 'd20+6', or 'd20'"
			continue
		if arguments[0] == '':
			arguments[0] = '1'
		arguments = [int(x) for x in arguments]
		

		results = get_roll(*arguments)
		
		u_results = ''
		if c:
			u_results = []
			for x in results:
				u_results.append(update(c,x,int(modifier)))

		ts = time.time()
		dt = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
		
		
		al = [o_arguments, dt,r_number]


		print message.format(*al), results, u_results
		r_number += 1
