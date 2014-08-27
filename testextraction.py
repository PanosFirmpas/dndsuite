import pandas as pd

def xcontainsy(x,y):
	x,y = str(x),str(y)
	if y in x:
		return True
	else:
		return False

def xnotcontainsy(x,y):
	x,y = str(x),str(y)
	if y in x:
		return False
	else:
		return True

def print_spell(id):
	spell = df.iloc[id]

	print spell['name']
	print spell.level, spell.type, spell.ritual
	print spell.casting_time, spell.casting_time_comment
	print spell.range
	print spell.components, spell.components_comment
	print spell.duration, spell.duration_comment
	print spell.discription
	print



df = pd.io.parsers.read_csv(open('./spells.txt'),sep=';')

print len(df)

keys = 'name','level','type','ritual','casting_time','casting_time_comment','range','components','components_comment','duration','duration_comment','discription'

key = 'discription'
arg = '-'

def isx(x):
	if not x:
		return False
	if len(x) <5:
		return False
	return True

# criterion = df[key].map(lambda x: xcontainsy(x,arg))
criterion = df[key].map(lambda x: not isx(x) )

print df[criterion]
# print_spell(18)
# print_spell(19)
# print_spell(20)


