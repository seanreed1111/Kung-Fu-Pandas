'''
This program takes a letter input and determines whether it's a vowel or consonant
'''
def letter():
	let = input("Please enter a letter: ")                           #Take letter input from user
	vow = ("a", "e", "i", "o", "u")                                  #Define tuple with vowels

	if let in vow:                                                   #Check if leter is in tuple. If yes then it's a vowel
		print("The letter \"" + let + "\" is vowel.")
	elif let == "y":
		print("The letter \"y\" sometimes can be a vowel and " + \
			"sometime a consonant")                                  #If letter is y - special case
	else:                                                            #Otherwise we have consonant
		print("The letter \"" + let + "\" is a consonant")

letter()