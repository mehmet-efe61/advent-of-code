numbers=[]
number25=[]
# with open ('inputday9.txt') as inputtext:
# 	for line in inputtext:
# 		numbers.append(int(line.strip()))

# for i in range(5):
# 	number25.append(numbers[i])
# a=5
# valid=0
# while a<len(numbers):
# 	int1=numbers[a]
# 	valid=0
# 	for i in number25:
# 		for b in number25:
# 			if i != b:
# 				if (i+b) == int1:
# 					valid=1
# 	if valid == 0:
# 		print(int1)
# 	number25.pop(0)
# 	number25.append(numbers[a])
# 	a+=1

with open ('inputday9.txt') as inputtext:
	for line in inputtext:
		numbers.append(int(line.strip()))

for i in range(len(numbers)):
	sum=numbers[i]
	number25.append(numbers[i])
	for a in range(i+1, len(numbers)):
		sum+=numbers[a]
		number25.append(numbers[a])
		if sum == 15690279:
			print(sum)
			print(number25)
			number25.sort()
			print(number25[0]+number25[-1])
	number25.clear()