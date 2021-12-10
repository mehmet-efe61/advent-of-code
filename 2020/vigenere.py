from sys import exit

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt():
	global laststr
	for i in range(len(text)):
		cipher_index = alphabet.index(text[i])+alphabet.index(altkeyword[i])
		if cipher_index>25:
			cipher_index-=26
		laststr+=alphabet[cipher_index]

def decrypt():
	global laststr
	for i in range(len(text)):
		index_text=alphabet.index(text[i])
		index_keyword=alphabet.index(altkeyword[i])
		if index_text>index_keyword:
			index_org=index_text-index_keyword
		elif index_text<index_keyword:
			index_org=26-index_keyword+index_text
		else:
			index_org=0
		laststr+=alphabet[index_org]

option=str(input('(d)ecrypt or (e)ncrypt? '))
textinput=str(input('text to process: '))
keyword=str(input('keyword: '))

altkeyword=keyword
text=textinput.replace(' ', '')
texttemplate=textinput.split(' ')
lastlength=0
laststr=''

for i in range(len(text)):
	if len(altkeyword) < len(text):
		altkeyword += altkeyword[i]

if option == 'e':
	encrypt()
elif option == 'd':
	decrypt()
else:
	print('try again')
	exit()

for i in texttemplate:
	print(laststr[lastlength:lastlength+len(i)], end=' ')
	lastlength+=len(i)
print()
