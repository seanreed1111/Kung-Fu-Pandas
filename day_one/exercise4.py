def letter():
	let = input("Please enter a letter: ")
	vow = ["a", "e", "i", "o", "u"]

	if let in vow:
		print("The letter \"" + let + "\" is vowel.")
	elif let == "y":
		print("The letter \"y\" sometimes can be a vowel and " + \
			"sometime a consonant")
	else:
		print("The letter \"" + let + "\" is a consonant")

letter()