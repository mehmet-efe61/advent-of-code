seats=[]
seatid=[]
with open ('inputday5.txt') as inputtext:
	for line in inputtext:
		seats.append(line.strip())
row=[0,128]
column=[0,8]

for i in seats:
	row=[0,127]
	column=[0,7]
	for a in i:
		if a == 'F':
			row[1]=(row[0]+row[1])/2
			row[1]=int(row[1]-(row[1]-int(row[1])))
		elif a == 'B':
			row[0]=(row[0]+row[1])/2
			row[0]=int(row[0]+(row[0]-int(row[0])))
		elif a == 'L':
			column[1]=(column[0]+column[1])/2
			column[1]=int(column[1]-(column[1]-int(column[1])))
		elif a == 'R':
			column[0]=(column[0]+column[1])/2
			column[0]=int(column[0]+(column[0]-int(column[0])))
	seatid.append(row[0]*8+column[0])

print(seatid)
print(max(seatid))