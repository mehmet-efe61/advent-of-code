alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

texttoencrypt=str(input('text to encrypt: '))
keyword=str(input('keyword: '))
newkeyword=keyword

texttoencrypt2=texttoencrypt.replace(' ', '')
textlength=len(texttoencrypt2)

for i in range(textlength):
	if len(newkeyword)<textlength:
		newkeyword+=newkeyword[i]
print(newkeyword)
laststr=''
for i in range(textlength):
	selecttext=texttoencrypt2[i]
	selectkeyword=newkeyword[i]
	index1=alphabet.index(selecttext)
	index2=alphabet.index(selectkeyword)
	if index1>index2:
		index3=index1-index2
	elif index1<index2:
		index3=26-index2+index1
	else:
		index3=0
	laststr+=alphabet[index3]

lastlength=0


texttoencrypt3=texttoencrypt.split(' ')
for i in texttoencrypt3:
	print(laststr[lastlength:lastlength+len(i)], end=' ')
	lastlength+=len(i)

print()







# textlength=len(texttoencrypt2)
# laststr=''
# for i in range(textlength):
# 	if len(newkeyword)<textlength:
# 		newkeyword+=newkeyword[i]
# 	selecttext=texttoencrypt2[i]
# 	selectkeyword=newkeyword[i]
# 	index1=alphabet.index(selecttext)
# 	index2=alphabet.index(selectkeyword)
# 	cypherindex=index1+index2
# 	if cypherindex>25:
# 		cypherindex-=26
# 	laststr+=alphabet[cypherindex]

# print(laststr)


# texttoencrypt3=texttoencrypt.split(' ')

# originallength=len(texttoencrypt3)
# lastlength=0

# for i in texttoencrypt3:
# 	print(laststr[lastlength:lastlength+len(i)], end=' ')
# 	lastlength+=len(i)

# print()

