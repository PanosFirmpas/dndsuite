import re

lines = []

with open('./npdfspells.txt','r') as f:
	count = 0
	for line in f:
		count += 1
		if '-level' in line or 'cantrip' in line:
			lines.append(count)
print len(lines)
with open('./npdfspells.txt','r') as f:
	# with open('./npdfspells.txt','w') as fo:

		count = 0
		sc = 0
		for line in f:
			count += 1
			if count+1 in lines:
				if  re.search('[a-zA-Z]\s[a-zA-Z]\s',line.rstrip()):
					split = line.rstrip().split(' ')
					for x in split:
						if len(x)>1:
							break
					else:
						sc +=1 
						# print line
			# fo.write(line)
print sc

# with open('./npdfspells.txt','r') as f:
# 	c = 0
# 	for line in f:

# 		if re.search('[a-zA-Z]\s[a-zA-Z]\s[a-zA-Z]\s',line.rstrip()):
			
# 			split = line.rstrip().split(' ')
# 			for x in split:
# 				if len(x)>1:
# 					break
# 			else:
# 				c += 1
# 				# print line
# 				n = f.next()
# 				if not '-level' in n and not 'cantrip' in n:
# 					print line


# print c