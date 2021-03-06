import pandas
import re

def identify_name(line):
	if  re.search('[a-zA-Z]\s[a-zA-Z]\s',line.rstrip()):
					split = line.rstrip().split(' ')
					for x in split:
						if len(x)>1:
							return False
					else:
						name = ' '.join(split)
						name = name.replace('  ','#')
						name = name.replace(' ','')
						name = name.replace('#',' ')


						return name
			

def identify_level_stype(line):
	# split = line.rstrip().split(' ')
	if 'cantrip' in line:
			ritual = True if '(ritual)' in line else None

			return 0,line.split(' ')[0],ritual
	elif '-level' in line:
		ritual = True if '(ritual)' in line else None
		if ritual:
			split = line.rstrip().split(' ')[:-1]
		else:
			split = line.rstrip().split(' ')
		
		if len(split) == 3:
			level,junk,stype = split
			level = int(level)
		elif len(split) == 2:
			
			level,stype = split
			
			level = int(level[:1])
		else:
			print split
		return level,stype,ritual

	return False,False,False

def identify_casting_time(line):
	if line.startswith('Casting Tim'):
		orr = None

		if re.search('1\s*action',line):
			ct = line.split(': ')[1]
			if 'or' in line:
				ct,orr = line.split(': ')[1].split('or')
		elif re.search('1\s*bonus\s*action',line):
			ct = '1 bonus action'

		elif re.search('10\s*minutes',line):
			ct = '10 minutes'
		elif re.search('minute',line):
			ct = '1 minute'
		elif '1  hour' in line:
			ct = '1 hour'
		elif '24' in line:
			ct = '24 hours'

		elif re.search('8\s*hours',line):
			ct = '8 hours'
		elif '12' in line:
			ct = '12 hours'
		elif re.search('1\s*reaction',line):
			print line
			ct = '1 reaction'
			orr = line.split(',')[1]
		else:
			print [line]
		return ct,orr
	else:
		return None,None
			
def identify_range(line):
	if line.startswith('Range:') or line.startswith('Ran ge:'):
		r = None
		if 'Touch' in line or 'Tou ch' in line:
			r = 'touch'
		elif 'Sight' in line:
			r = 'sight'
		elif 'Self' in line or 'S elf' in line:
			r = 'self'
		elif re.search('1\s*mile',line):
			r = '1 mile'
		elif 'Special' in line:
			r = 'special'
		elif '500 miles' in line:
			r = '500 miles'
		elif re.search('Unlimited',line):
			r = 'Unlimited'

		elif 'feet' in line:
			r = line.rstrip().split(': ')[1]
		else:
			print "range error: ",line
			

		return r
	else:
		return None

def identify_components(line):
	if line.startswith('Components'):
		comment = None
		comps = []
		if 'V' in line:
			comps.append('V')
		if 'S' in line:
			comps.append('S')
		if 'M' in line:
			comps.append('M')
			comment = '('+line.rstrip().split('(')[1]
			
		return comps,comment
	else:
		return False,False

def identify_duration(line):
	
	if line.startswith('Duration: '):
		
		comment = None
		
		if True in [(x in line) for x in ['1  round','1 r ound', '1 round', '1 h ou r','1 roun d']]:
			dur = '1 round'
		elif True in [(x in line) for x in ['In stan tan','Instantaneous']]:
			dur = 'instant'
		elif True in [(x in line) for x in ['1  minute', '1 minute','1 m inute']]:
			dur = '1 minutes'
		elif True in [(x in line) for x in ['1 h our','1 hour','1  hour']]:
			dur = '1 hour'
		elif re.search('Concentration,',line):
			dur = 'concentration'
			comment = line.rstrip().split(',')[1]
			print comment

		elif True in [(x in line) for x in ['10  minutes', '10 minutes']]:
			dur = '10 minutes'
		elif True in [(x in line) for x in ['8 hours','8 h ours','8 h ou rs']]:
			dur = '8 hours'
		elif True in [(x in line) for x in ['24']]:
			dur = '24 hours'
		elif True in [(x in line) for x in ['10 days']]:
			dur = '10 days'
		elif True in [(x in line) for x in ['30 days']]:
			dur = '30 days'
		elif True in [(x in line) for x in ['7 days']]:
			dur = '7 days'
		elif True in [(x in line) for x in ['Special']]:
			dur = 'special'
		elif True in [(x in line) for x in ['Until']]:

			dur = 'Until dispelled or triggered'
		elif True in [(x in line) for x in ['1  day']]:

			dur = '1 day'
			

		else:
			print "##",line

		return dur,comment
	else:
		return False,False

def get_spells(f):
	spells = {}
	line = f.next()
	while 1:
		

		name =  identify_name(line)
		if name:
			c_name = name
			spells[name] = {}
			discription = []
			line = f.next()

			

		level,stype,ritual  = identify_level_stype(line)
		if stype:
			stype = stype.lower()
			spells[c_name]['level'] =  level
			spells[c_name]['type'] =  stype
			if ritual:
				spells[c_name]['ritual'] =  True
			line = f.next()
			

		
		casting_time,orr =  identify_casting_time(line)
		if casting_time:
			spells[c_name]['casting_time'] =  casting_time
			if orr:
				line = f.next()
				while not line.startswith('Range'):
					orr += line
					line = f.next()
				
				spells[c_name]['casting_time_comment'] =  orr
			else:
				line = f.next()
			

		rrange = identify_range(line)
		if rrange:
			
			spells[c_name]['range'] =  rrange
			line = f.next()
			

		comps,comment = identify_components(line)
		if comps:
			spells[c_name]['components'] =  ','.join(comps)
			if comment:
				line = f.next()
				
				while not line.startswith('Duration'):
					comment += line.rstrip()
					line = f.next()
				
				spells[c_name]['components_comment'] =  comment[:-1]
				
			else:
				line = f.next()

		duration,comment = identify_duration(line)
		if duration:
			spells[c_name]['duration'] =  duration
			if comment:
				
				spells[c_name]['duration_comment'] =  comment
			
			line = f.next()

		
		discription = line

		while not identify_name(line):
			discription += (line)
			try:
				line = f.next()
			except:
				spells[c_name]['discription'] =  ''.join(discription)
				return spells
				pass

		else:
			spells[c_name]['discription'] =  ''.join(discription)


with  open('./npdfspells.txt.','r') as f:
	spells = get_spells(f)

columns = ['name','level','type','ritual','casting_time','casting_time_comment', 'range','components','components_comment','duration','duration_comment','discription']






with open('./spells.txt','w') as f:
	f.write(';'.join(columns)+'\n')

	for k in sorted(spells.keys()):
		v = spells[k]
		tp = [k]
		for x in columns[1:]:
			tp.append(str(v.get(x,'-')))
		
		f.write(';'.join(tp).replace('\n','')+'\n' )








# spells = pandas.DataFrame.from_csv('./spells.txt', sep=';')
# print spells[spells['level'] == '9']
# 



		



	


			



		