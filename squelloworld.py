original = input('Enter a word: ')
word = original.lower()

def sq_word (word):
	if len(word) > 0 and word.isalpha():
		if word[0] in ['a', 'e', 'i', 'o', 'u', 'w']:
			print ('Squ' + word)
		elif word[0] != ['a', 'e', 'i', 'o', 'u', 'w']:
			print ("Squ" + word[1:])
	else:
		print ("Try again my squirly friend!")

sq_word(word)
