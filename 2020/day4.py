passport=[]

field=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

validfinal=0

with open ('inputday4.txt') as inputtext:
	for line in inputtext:
		temparray=line.split()
		for i in temparray:
			passport.append(i)
		if line == '\n':
			count=0
			for a in passport:
				for b in field:
					if a.split(':')[0] == b:
						count+=1
			if count==7:
				valid=0
				for i in passport:
					tempsplit=i.split(':')
					if tempsplit[0] == 'byr':
						if int(tempsplit[1])>=1920 and int(tempsplit[1])<=2002:
							valid+=1

					elif tempsplit[0] == 'iyr':
						if int(tempsplit[1])>=2010 and int(tempsplit[1])<=2020:
							valid+=1

					elif tempsplit[0] == 'eyr':
						if int(tempsplit[1])>=2020 and int(tempsplit[1])<=2030:
							valid+=1

					elif tempsplit[0] == 'eyr':
						if int(tempsplit[1])>=2020 and int(tempsplit[1])<=2030:
							valid+=1

					elif tempsplit[0] == 'hgt':
						if tempsplit[1][-2:] == 'cm':
							if int(tempsplit[1][:-2])>=150 and int(tempsplit[1][:-2])<=193:
								valid+=1
						elif tempsplit[1][-2:] == 'in':
							if int(tempsplit[1][:-2])>=59 and int(tempsplit[1][:-2])<=76:
								valid+=1

					elif tempsplit[0] == 'hcl':
						valide=0
						if tempsplit[1][0] == '#':
							if len(tempsplit[1][1:]) == 6:
								for e in tempsplit[1]:
									if e in '#0123456789abcdef':
										valide+=1
								if valide==7:
									valid+=1

					elif tempsplit[0] == 'ecl':
						if tempsplit[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
							valid+=1

					elif tempsplit[0] == 'pid':
						if len(tempsplit[1]) == 9:
							valid+=1

				if valid==7:
					validfinal+=1
			passport.clear()
print(validfinal)

