volt=[]
volt2=[]

with open ('inputday10.txt') as inputtext:
	for line in inputtext:
		volt.append(int(line.strip()))

volt.sort()
volt.insert(0,0)
volt.append(volt[-1]+3)

for i in range(1, len(volt)):
	


# j1=0
# j3=0

# for i in range(1, len(volt)):
# 	diff=volt[i]-volt[i-1] 
# 	if diff==1:
# 		j1+=1
# 	elif diff==3:
# 		j3+=1

print(j1)
print(j3)
print(j1*j3)