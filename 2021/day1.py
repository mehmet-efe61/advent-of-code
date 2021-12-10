#1
depth=[]
many=0
with open("day1.txt") as inputtext:
	for line in inputtext:
		depth.append(int(line.strip()))

for i in range(1, len(depth)):
	if (depth[i]) > (depth[i-1]):
		many+=1
print(many)

#2
numsum=[]
while True:
	for i in range(3)
		print(i)