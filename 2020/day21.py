# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)

with open('inputday21.txt') as inputfile:
	f=inputfile.readlines()
allfoods=[]
allingds=[]
for i in f:
	allfoods.append(i.split(' (')[0].split())
for i in f:
	allingds.append(i.split('contains ')[1].split(')')[0].split(', '))


# food1="mxmxvkd kfcds sqjhc nhms (contains dairy, fish)"
# food2="trh fvjkl sbzzf mxmxvkd (contains dairy)"
# ingds=food1.split(' (')[0].split()
# ingdseng=food1.split('contains ')[1].split(')')[0].split(', ')
# ingds2=food2.split(' (')[0].split()
# ingds2eng=food2.split('contains ')[1].split(')')[0].split(', ')
# ingds=[[['mxmxvkd', 'kfcds', 'sqjhc', 'nhms'], ['dairy', 'fish']], [['trh', 'fvjkl', 'sbzzf', 'mxmxvkd']]]
foods={}
for new in range(len(allfoods)):
	for a in allfoods[new]:
		for new2 in range(new, len(allfoods)):
			for b in allfoods[new2]:
				if a == b:
					for new3 in range(len(allingds)):
						for c in allingds[new3]:
							for new4 in range(new3, len(allingds)):
								for d in allingds[new4]:
									if c == d:
										foods[c]=a

print(foods)
