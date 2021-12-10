array=[]
with open ('inputday3.txt') as inputtext:
	for line in inputtext:
		array.append(line.strip())

#print(array)
b=0

def findtrees():
	global b
	count=0
	for a in range(2,len(array),2):
		b+=1
		while b>30:
			b-=31
		if array[a][b] == '#':
			count+=1
	return count

print(findtrees())


#16309800





# def findtrees(slope):
# 	global b
# 	count=0
# 	a=1
# 	while a<len(array):
# 		b+=slope
# 		while b>30:
# 			b-=31
# 		if array[a][b] == '#':
# 			count+=1
# 		a+=1
# 	return count

# print(findtrees(1))
