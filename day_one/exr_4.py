def alphabets():
	x = input("Enter the alphabet: ")
	list_of_vowels= ['a', 'e', 'i', 'o', 'u']
	
	if x == 'y':
		print("y is sometime a vowel and sometime a consonant")

	elif x in list_of_vowels:
		print("It is a vowel")
	else:
		print("It is a consonant")

alphabets()