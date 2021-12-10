inst=[]
inst2=[]
value=0
i=0

with open ('inputday8.txt') as inputtext:
	for line in inputtext:
		inst.append(line.strip())
for a in range(len(inst)):
	if 'nop' in inst[a]:
		inst[a]='jmp '+inst[a].split()[1].strip()
		print(inst[a])
	elif 'jmp' in inst[a]:
		inst[a]='nop '+inst[a].split()[1].strip()
		print(inst[a])
	else:
		continue
	while i<len(inst):
		inst2.append(i)
		if 'nop' in inst[i]:
			i+=1
			print(i)
			continue
		if 'acc' in inst[i]:
			value+=int(inst[i].split()[1])
			i+=1
			print(i)
		if 'jmp' in inst[i]:
			i+=int(inst[i].split()[1])
			print(i)
	if i == len(inst):
		break
print(inst)
print(inst2)
print(value)